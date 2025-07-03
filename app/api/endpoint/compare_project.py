from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.schemas.compare_project_dto import CompareRequest, CompareResponse, CompareResult
from app.core.database import get_session
from app.ml.model_loader import get_model
from app.ml.similarity_compare import compute_cosine_score
from app.ml.text_encoder import encode_fields
from app.models.project_embeddings import ProjectEmbedding
from app.models.field_weights import FieldWeights
import json
from collections import defaultdict

router = APIRouter()

@router.post("/compare-project", response_model=CompareResponse)
def compare_project(request: CompareRequest, session: Session = Depends(get_session)):
    model = get_model()
    
    #1. Encode input fields
    input_embeddings = encode_fields(request.fields)
    
    # 2. Load all existing project embeddings that match the semester and campusId
    statementQuery = select(ProjectEmbedding).where(
        ProjectEmbedding.IsDeleted == False,
        ProjectEmbedding.SemesterName.in_(request.semesters),
        ProjectEmbedding.CampusId == request.campusId
    )
    
    all_embeddings = session.exec(statementQuery).all()
    
    # 3. Load weights
    weight_statement = select(FieldWeights).where(FieldWeights.IsDeleted==False)
    
    weights ={w.FieldName: w.WeightValue for w in session.exec(weight_statement)}
    
    # 4. Arrange embeddings follow ProjectId
    projects_dict = defaultdict(dict)
    
    for item in all_embeddings:
        try:
            emb = json.loads(item.EmbeddingJson)
            projects_dict[item.ProjectId][item.FieldName] = emb
        except Exception as e:
            print("Error in: ", item.FieldName)
            print("Eror: ", e)
            continue
        
    # 5. Tính điểm từng Project
    results = []
    for project_id, fields in projects_dict.items():
        total_score = 0.0
        total_weight = 0.0
        
        for field, input_vec in input_embeddings.items():
            if field in fields:
                sim = compute_cosine_score(input_vec, fields[field])
                weight = weights.get(field)
                total_score += sim*weight
                total_weight +=weight
                
        if total_weight >0:
                results.append(CompareResult(ProjectId= project_id, Score=round((total_score/ total_weight),4)))
                
    # 6. Lấy các Score >=0.6 và Sắp xếp kết quả
    filtered_results = [res for res in results if res.Score >= 0.6]
    
    sorted_results = sorted(filtered_results, key=lambda x: x.Score, reverse=True)

    # Lấy top 5 kết quả với điểm cao nhất
    top_5_results = sorted_results[:5]
    
    return CompareResponse(results=sorted_results)
    
    


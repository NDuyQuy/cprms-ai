import numpy as np
from app.ml.model_loader import get_model
import json
from sentence_transformers import SentenceTransformer

model = get_model()
def compute_cosine_score(vec1, vec2_json): #vec1 là cần so sánh đã encode, còn vec2 lấy từ db ra phải deserialization sang vectvor
    
    
    vec2 = np.array(json.loads(vec2_json), dtype=np.float32)
    
    vec1 = np.array(vec1, dtype=np.float32).reshape(1,-1)
    vec2 = vec2.reshape(1,-1)
    
    similarities = model.similarity(vec1, vec2)
    
    return float(similarities[0][0])

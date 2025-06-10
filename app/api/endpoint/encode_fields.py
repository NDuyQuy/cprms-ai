from fastapi import APIRouter
from app.schemas.encode_fields_dto import FieldEncodeRequest, FieldEncodeResponse
from app.ml.text_encoder import encode_fields

router = APIRouter()

@router.post("/encode-fields", response_model=FieldEncodeResponse)
def encode_fields_endpoint(request : FieldEncodeRequest):
    embeddings = encode_fields(request.fields)
    return FieldEncodeResponse(embeddings=embeddings)
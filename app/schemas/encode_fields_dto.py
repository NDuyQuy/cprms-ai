from pydantic import BaseModel
from typing import Dict

class FieldEncodeRequest(BaseModel):
    fields: Dict[str, str] #field_name: cleaned_text from .net
    
class FieldEncodeResponse(BaseModel):
    embeddings: Dict[str, str]  # field_name: embedding_stringified
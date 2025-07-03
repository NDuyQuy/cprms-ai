from pydantic import BaseModel
from typing import Dict, List

class CompareRequest(BaseModel):
    fields: Dict[str, str]  # { "EnglishName": "abc", "ContextObjectives": "xyz" }
    semesters: List[str] # Danh sách kỳ cần so sánh (Ví dụ: ["SU25", "SP25"])
    campusId: str # campus hiện tại cần so sánh khi user login vào
class CompareResult(BaseModel):
    ProjectId: str
    Score: float

class CompareResponse(BaseModel):
    results: List[CompareResult]

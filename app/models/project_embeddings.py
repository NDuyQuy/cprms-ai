from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class ProjectEmbedding(SQLModel, table=True):
    __tablename__ = 'ProjectEmbedding'

    Id: str = Field(primary_key=True)
    ProjectId: str
    FieldName: str
    EmbeddingJson: str
    ModelVersion: Optional[str]

    CreatedAt: Optional[datetime]
    CreatedBy: Optional[str]
    LastModified: Optional[datetime]
    LastModifiedBy: Optional[str]
    RowVersion: Optional[bytes]
    IsDeleted: bool
    SemesterName: str
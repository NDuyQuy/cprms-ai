from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class FieldWeights(SQLModel, table=True):
    __tablename__ = 'FieldWeights'
    Id: str = Field(primary_key=True)
    FieldName: str
    WeightValue: int
    SpecialtyId: int
    CreatedAt: Optional[datetime]
    CreatedBy: Optional[str]
    LastModified: Optional[datetime]
    LastModifiedBy: Optional[str]
    RowVersion: Optional[bytes]
    IsDeleted: bool
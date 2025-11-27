# backend/schemas.py
from pydantic import BaseModel, EmailStr


class ProfessorBase(BaseModel):
    nome: str
    email: EmailStr


class ProfessorCreate(ProfessorBase):
    senha: str


class ProfessorLogin(BaseModel):
    email: EmailStr
    senha: str


class ProfessorOut(ProfessorBase):
    id: int

    class Config:
        # FastAPI 0.1x / Pydantic v2
        from_attributes = True

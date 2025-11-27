# backend/schemas.py
from pydantic import BaseModel, EmailStr


# ---------------------- PROFESSOR ----------------------


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


# ---------------------- ALUNO ----------------------


class AlunoBase(BaseModel):
    nome: str


class AlunoCreate(AlunoBase):
    academia_id: int


class AlunoOut(AlunoBase):
    id: int
    codigo: str
    academia_id: int

    class Config:
        from_attributes = True


class LoginAlunoRequest(BaseModel):
    codigo: str

# backend/aluno_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import random

from .database import get_db
from . import models, schemas

router = APIRouter(
    prefix="/alunos",
    tags=["alunos"]
)


def gerar_codigo():
    """
    Gera um código de acesso no formato GTJ-123456
    """
    return f"GTJ-{random.randint(100000, 999999)}"


@router.post("/", response_model=schemas.AlunoOut)
def criar_aluno(payload: schemas.AlunoCreate, db: Session = Depends(get_db)):
    """
    Cria um aluno vinculado a uma academia e gera um código GTJ-XXXXXX.
    (Depois o painel do professor vai chamar essa rota.)
    """
    codigo = gerar_codigo()

    aluno = models.Aluno(
        nome=payload.nome,
        academia_id=payload.academia_id,
        codigo=codigo
    )

    db.add(aluno)
    db.commit()
    db.refresh(aluno)

    return aluno


@router.post("/login", response_model=schemas.AlunoOut)
def login_aluno(payload: schemas.LoginAlunoRequest, db: Session = Depends(get_db)):
    """
    Login do aluno via código de acesso.
    """
    aluno = (
        db.query(models.Aluno)
        .filter(models.Aluno.codigo == payload.codigo)
        .first()
    )

    if not aluno:
        raise HTTPException(
            status_code=404,
            detail="Código não encontrado. Verifique com a sua academia."
        )

    return aluno

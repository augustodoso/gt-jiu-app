from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import List, Dict

from .database import Base, engine, SessionLocal
from .models import (
    Usuario, UsuarioCreate, UsuarioLogin,
    Academia, AcademiaCreate, AcademiaOut,
    Medalha, MedalhaCreate, MedalhaOut,
    CategoriaRequest, CategoriaResponse,
    RankingAcademia,
)

import hashlib

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(title="GT Jiu - Aurevix MVP")

# CORS liberado para o frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBearer()

# token -> id_usuario
TOKENS: Dict[str, int] = {}


# ---------- DEPENDÊNCIA DE DB ----------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------- AUTENTICAÇÃO SIMPLES (MVP) ----------

def criar_token(user: Usuario) -> str:
    """
    Gera um token simples baseado em email+senha.
    NÃO é seguro para produção, mas serve para MVP/local.
    """
    raw = f"{user.email}{user.senha}"
    token = hashlib.sha256(raw.encode()).hexdigest()
    TOKENS[token] = user.id
    return token


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
) -> Usuario:
    token = credentials.credentials
    user_id = TOKENS.get(token)
    if not user_id:
        raise HTTPException(status_code=403, detail="Token inválido ou expirado.")
    user = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not user:
        raise HTTPException(status_code=403, detail="Usuário não encontrado.")
    return user


@app.post("/register")
def registrar_usuario(payload: UsuarioCreate, db: Session = Depends(get_db)):
    # Verifica se já existe e-mail
    existente = db.query(Usuario).filter(Usuario.email == payload.email).first()
    if existente:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado.")

    user = Usuario(
        nome=payload.nome,
        email=payload.email,
        senha=payload.senha,  # senha simples (MVP)
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = criar_token(user)
    return {"message": "Usuário cadastrado", "token": token, "nome": user.nome}


@app.post("/login")
def login(payload: UsuarioLogin, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.email == payload.email).first()
    if not user or user.senha != payload.senha:
        raise HTTPException(status_code=401, detail="Credenciais inválidas.")

    token = criar_token(user)
    return {"message": "Login efetuado", "token": token, "nome": user.nome}


# ---------- CATEGORIA (IDADE + PESO) ----------

def classificar_peso_cbjj(idade: int, peso: float, sexo: str):
    # Faixa etária simplificada
    if idade < 16:
        faixa_etaria = "Infantil / Juvenil 1"
    elif idade < 18:
        faixa_etaria = "Juvenil 2"
    elif idade <= 29:
        faixa_etaria = "Adulto"
    else:
        faixa_etaria = "Master"

    s = sexo.upper()

    # Pesos aproximados da tabela CBJJ (adulto), masculino e feminino
    if s == "M":
        if peso <= 57.5:
            categoria = "Galo"
        elif peso <= 64.0:
            categoria = "Pluma"
        elif peso <= 70.0:
            categoria = "Pena"
        elif peso <= 76.0:
            categoria = "Leve"
        elif peso <= 82.3:
            categoria = "Médio"
        elif peso <= 88.3:
            categoria = "Meio-Pesado"
        elif peso <= 94.3:
            categoria = "Pesado"
        elif peso <= 100.5:
            categoria = "Super-Pesado"
        else:
            categoria = "Pesadíssimo"
    elif s == "F":
        if peso <= 48.5:
            categoria = "Galo"
        elif peso <= 53.5:
            categoria = "Pluma"
        elif peso <= 58.5:
            categoria = "Pena"
        elif peso <= 64.0:
            categoria = "Leve"
        elif peso <= 69.0:
            categoria = "Médio"
        elif peso <= 74.0:
            categoria = "Meio-Pesado"
        elif peso <= 79.3:
            categoria = "Pesado"
        else:
            categoria = "Super-Pesado / Pesadíssimo"
    else:
        categoria = "Indefinida"

    return faixa_etaria, categoria


@app.post("/categoria", response_model=CategoriaResponse)
def calcular_categoria(req: CategoriaRequest):
    faixa_etaria, categoria_peso = classificar_peso_cbjj(req.idade, req.peso, req.sexo)
    return CategoriaResponse(
        faixa_etaria=faixa_etaria,
        categoria_peso=categoria_peso,
        observacao=(
            "Classificação baseada em faixas de peso semelhantes à tabela CBJJ/IBJJF "
            "(peso máximo por categoria, com kimono). "
            "Sempre confira o regulamento específico do campeonato."
        ),
    )


# ---------- ACADEMIAS ----------

@app.post("/academias", response_model=AcademiaOut)
def criar_academia(
    academia: AcademiaCreate,
    db: Session = Depends(get_db),
    user: Usuario = Depends(get_current_user),  # precisa estar logado
):
    db_acad = Academia(**academia.dict())
    db.add(db_acad)
    db.commit()
    db.refresh(db_acad)
    return db_acad


@app.get("/academias", response_model=List[AcademiaOut])
def listar_academias(
    cidade: str | None = None,
    bairro: str | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(Academia)
    if cidade:
        query = query.filter(Academia.cidade == cidade)
    if bairro:
        query = query.filter(Academia.bairro == bairro)
    return query.all()


# ---------- MEDALHAS ----------

@app.post("/medalhas", response_model=MedalhaOut)
def criar_medalha(
    medalha: MedalhaCreate,
    db: Session = Depends(get_db),
    user: Usuario = Depends(get_current_user),  # precisa estar logado
):
    db_med = Medalha(**medalha.dict())
    db.add(db_med)
    db.commit()
    db.refresh(db_med)
    return db_med


@app.get("/medalhas", response_model=List[MedalhaOut])
def listar_medalhas(
    academia_id: int | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(Medalha)
    if academia_id:
        query = query.filter(Medalha.academia_id == academia_id)
    return query.all()


# ---------- RANKING ----------

@app.get("/ranking/academias", response_model=List[RankingAcademia])
def ranking_academias(db: Session = Depends(get_db)):
    academias = db.query(Academia).all()
    resultado: List[RankingAcademia] = []

    for acad in academias:
        medalhas = acad.medalhas
        ouro = sum(1 for m in medalhas if m.tipo_medalha == "ouro")
        prata = sum(1 for m in medalhas if m.tipo_medalha == "prata")
        bronze = sum(1 for m in medalhas if m.tipo_medalha == "bronze")
        total = ouro + prata + bronze

        resultado.append(
            RankingAcademia(
                academia_id=acad.id,
                nome_academia=acad.nome,
                ouro=ouro,
                prata=prata,
                bronze=bronze,
                total=total,
            )
        )

    resultado.sort(key=lambda r: r.total, reverse=True)
    return resultado

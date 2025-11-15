from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel, EmailStr, validator
from datetime import date
from typing import Optional
from .database import Base
import re

# ---------------------- MODELOS SQLALCHEMY ----------------------


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True, index=True)
    senha = Column(String)


class Academia(Base):
    __tablename__ = "academias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    mestre = Column(String)
    cidade = Column(String)
    bairro = Column(String)
    telefone = Column(String)
    endereco = Column(String)
    email = Column(String)

    medalhas = relationship("Medalha", back_populates="academia")


class Medalha(Base):
    __tablename__ = "medalhas"

    id = Column(Integer, primary_key=True, index=True)
    academia_id = Column(Integer, ForeignKey("academias.id"))
    faixa = Column(String)
    sexo = Column(String)
    categoria_peso = Column(String)
    tipo_medalha = Column(String)
    campeonato = Column(String)
    cidade_evento = Column(String)
    data_evento = Column(Date)
    comprovante_descricao = Column(String)
    status_validacao = Column(String, default="aprovado")

    academia = relationship("Academia", back_populates="medalhas")


# ---------------------- SCHEMAS PYDANTIC ----------------------


class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str


class UsuarioLogin(BaseModel):
    email: EmailStr
    senha: str


class AcademiaBase(BaseModel):
    nome: str
    mestre: str
    cidade: str
    bairro: str
    telefone: str
    endereco: str
    email: EmailStr

    @validator("telefone")
    def validar_telefone(cls, v: str) -> str:
        # Ex: (31) 99999-8888 ou 31999998888
        padrao = r"^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$"
        if not re.match(padrao, v):
            raise ValueError("Telefone inválido. Ex: (31) 99999-8888")
        return v


class AcademiaCreate(AcademiaBase):
    pass


class AcademiaOut(AcademiaBase):
    id: int

    class Config:
        orm_mode = True


class MedalhaBase(BaseModel):
    academia_id: int
    faixa: str
    sexo: str
    categoria_peso: str
    tipo_medalha: str
    campeonato: str
    cidade_evento: str
    data_evento: date
    comprovante_descricao: Optional[str] = None


class MedalhaCreate(MedalhaBase):
    pass


class MedalhaOut(MedalhaBase):
    id: int
    status_validacao: str

    class Config:
        orm_mode = True


class CategoriaRequest(BaseModel):
    idade: int
    peso: float
    sexo: str


class CategoriaResponse(BaseModel):
    faixa_etaria: str
    categoria_peso: str
    observacao: Optional[str] = None


class RankingAcademia(BaseModel):
    academia_id: int
    nome_academia: str
    ouro: int
    prata: int
    bronze: int
    total: int

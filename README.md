# 🥋 GT Jiu — Aurevix Tech  
### Plataforma completa para academias, professores e alunos de Jiu-Jitsu

> **Ranking • Academias • Medalhas • Categorias • Regras • Faixas • Painel do Professor • Painel do Aluno**

O **GT Jiu** é um MVP funcional desenvolvido para organizar o Jiu-Jitsu de forma profissional e moderna.  
Ele centraliza categorias, medalhas, ranking, academias, mensalidades, avisos e módulos educativos – tudo em um sistema rápido e intuitivo.

---

# 🚀 Deploys Oficiais

🔌 **API (FastAPI + Render)**  
https://gt-jiu-app.onrender.com

🖥️ **Frontend (GitHub Pages)**  
https://augustodoso.github.io/gt-jiu-app/

---

# 📌 Visão Geral

O GT Jiu nasceu para resolver um problema real:

✔ Organizar academias da cidade  
✔ Registrar medalhas e gerar ranking automaticamente  
✔ Facilitar o acesso do aluno via código  
✔ Criar um espaço educacional com regras, faixas e categoria IBJJF  
✔ Dar autonomia ao professor para gerenciar seus alunos  

É um **MVP pronto para se transformar em produto final**.

---

# 🧠 Funcionalidades

## 🥇 Ranking da Cidade do Jiu
- Cálculo automático baseado em:
  - 🥇 Ouro
  - 🥈 Prata
  - 🥉 Bronze  
- Atualização dinâmica conforme medalhas válidas  
- Ranking interno por academia e ranking geral  

---

## 🏅 Medalhas (com validação)
- Cadastro de medalhas pelo aluno  
- Validação pelo professor  
- Status:
  - **Aprovada**
  - **Pendente**
  - **Rejeitada**
- Computação automática no ranking  

---

## 🏫 Cadastro de Academias
Cada academia possui:
- Nome  
- Mestre responsável  
- Cidade e bairro  
- Endereço completo  
- Telefone  
- Observações  

---

## 🔐 Acesso do Aluno via Código
Cada aluno recebe um código único:
GTJ-XXXXXX


Esse código dá acesso ao painel com:
- Mensalidade  
- Ranking  
- Medalhas  
- Regras  
- Faixas  
- Conteúdos educativos  

---

## 🧮 Calculadora de Categoria (CBJJ)
Baseada em idade, peso e sexo:

- Faixa etária automática  
- Categoria IBJJF aproximada  
- Observações oficiais  

---

## 📚 Módulos Educativos
Inclui:
- Regras do Jiu-Jitsu (CBJJ/IBJJF-inspired)  
- Pontuações  
- Condutas  
- Hierarquia e faixas oficiais  
- Sistema alternativo com faixa amarela adulto (Federação Mineira)  

---

# 🛠️ Tecnologias Utilizadas

## **Backend**
- FastAPI  
- SQLAlchemy + SQLite  
- Python 3.11  
- Tokens de autenticação (MVP)  
- CORS liberado  
- Deploy no Render  

## **Frontend**
- HTML5  
- CSS3  
- JavaScript Puro  
- GitHub Pages  

## **Arquitetura**
- API REST  
- Páginas separadas por papéis (professor/aluno)  
- Login persistido no navegador  
- LGPD implementada com aceite obrigatório  

---

# 🧩 Estrutura do Projeto

gt-jiu-app/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── alunos_route.py      ← login por código
│   └── ...
│
├── frontend/
│   ├── index.html
│   ├── professor/
│   ├── aluno/
│   ├── css/
│   ├── img/
│   └── js/
│
├── requirements.txt
└── README.md


---

# 🧪 Como Rodar Localmente

## 1. Clone o repositório
```bash
git clone https://github.com/augustodoso/gt-jiu-app.git
cd gt-jiu-app

2. Crie o ambiente virtual
python -m venv venv

3. Ative

Windows:
venv\Scripts\activate

4. Instale as dependências
pip install -r requirements.txt

5. Rode o backend
uvicorn backend.main:app --reload

Acesse:
http://127.0.0.1:8000/docs

6. Rode o frontend
Abra:
frontend/index.html

🔐 LGPD

O projeto inclui:

Termo de aceite obrigatório

Política de privacidade

Armazenamento mínimo

Dados não compartilhados

Somente uso educacional

🧔 Desenvolvido por
Augusto Cezar — Aurevix Tech

Backend • IA • Cloud • Data • Frontend • Jiu-Jitsu Practitioner

🔗 LinkedIn:
https://www.linkedin.com/in/augusto-cezar-de-macedo-doso-38b83537

🔥 GitHub:
https://github.com/augustodoso

🤝 Contribuição

Contribuições são bem-vindas!
Sinta-se à vontade para abrir issues e PRs.



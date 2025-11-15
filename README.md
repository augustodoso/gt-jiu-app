# 🥋 GT Jiu — Aurevix  
### Ranking da Cidade do Jiu • Academias • Categorias • Medalhas • Regras • Hierarquia

O **GT Jiu — Aurevix** é um sistema completo para atletas e academias de Jiu-Jitsu organizarem **categorias**, **ranking por medalhas**, **registro de conquistas**, **pesquisa de regras**, **faixas e hierarquia** — tudo em uma plataforma moderna, leve e prática.

Este projeto nasceu para trazer **organização profissional** ao Jiu-Jitsu local, permitindo que qualquer cidade tenha seu próprio **Ranking da Cidade do Jiu**.

---

## 🚀 Funcionalidades

### 🥇 Ranking da Cidade do Jiu
- Ranking oficial das academias da cidade baseado em:
  - 🥇 Ouro  
  - 🥈 Prata  
  - 🥉 Bronze  
- Totalização automática das medalhas cadastradas.
- Ideal para criar um clima de competição saudável entre academias.

---

### 🥋 Classificação de Categoria (CBJJ-inspired)
O sistema calcula automaticamente:
- Faixa etária
- Categoria de peso (médio, leve, pesado, meio-pesado, etc.)
- Masculino / Feminino

Baseado na estrutura CBJJ e ajustado para uso prático dentro do app.

---

### 🏫 Cadastro de Academias
Cada academia pode cadastrar:
- Nome  
- Mestre responsável  
- Cidade & bairro  
- Telefone e e-mail  
- Endereço completo  

---

### 🏅 Registro de Medalhas
Para cada atleta:
- Academia
- Faixa
- Sexo
- Categoria de peso
- Tipo de medalha (ouro, prata, bronze)
- Campeonato
- Cidade do evento
- Data da competição
- Comprovante (link/descrição de ata, documento ou foto)

---

### 📚 Regras e Pontuações do Jiu-Jitsu
Inclui:
- Quedas  
- Raspagens  
- Passagem de guarda  
- Montada  
- Pegada de costas  
- Vantagens e punições  
- Critérios de encerramento da luta  
- Sistema de busca em tempo real  

Excelente para alunos tirarem dúvidas rapidamente.

---

### 🟦 Faixas, Hierarquia e Variações
Inclui:
- Sistema tradicional adulto (Branca → Azul → Roxa → Marrom → Preta)
- Sistema alternativo da **Federação Mineira** incluindo **faixa amarela para adultos**
- Explicações de conduta, respeito e postura dentro do tatame

---

## 🧠 Tecnologias Utilizadas

### **Backend**
- FastAPI
- SQLite + SQLAlchemy
- JWT Authentication
- CORS
- Deploy no **Render**

### **Frontend**
- HTML5, CSS3, JavaScript puro
- Consumo da API pública
- GitHub Pages

---

## 🌐 Deploys

### 🔌 API Backend (Render)
https://gt-jiu-app.onrender.com

### 🖥️ Frontend (GitHub Pages)
https://augustodoso.github.io/gt-jiu-app/

---

## 📦 Como rodar localmente

### 1. Clone o repositório
```bash
git clone https://github.com/augustodoso/gt-jiu-app.git
cd gt-jiu-app
```

### 2. Crie ambiente virtual
```bash
python -m venv venv
```

### 3. Ative o ambiente  
**Windows:**
```bash
venv\Scripts\activate
```

### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

### 5. Rode o backend
```bash
uvicorn backend.main:app --reload
```

Acesse:  
📍 http://127.0.0.1:8000/docs

### 6. Rode o frontend
Abra o arquivo:
```
index.html
```

---

## 🏛️ Arquitetura da Aplicação

```
gt-jiu-app/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── __init__.py
│
├── frontend/
│   └── index.html
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🤝 Contribuição

Contribuições são bem-vindas!  
Abra uma issue ou pull request com sugestões, melhorias ou correções.

---

## ✨ Criado por Aurevix
Um sistema desenvolvido com foco em:
- respeito ao Jiu-Jitsu  
- organização  
- ferramentas educacionais  
- incentivo às academias  

---

## 🥋 OSS 

---

## 🚀 Contato
Para dúvidas, sugestões ou parcerias, fale comigo no LinkedIn:

🔗 https://www.linkedin.com/in/augusto-cezar-de-macedo-doso-38b83537  

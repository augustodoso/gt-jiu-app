// =======================================
// CONFIGURAÇÃO DO BACKEND (RENDER)
// =======================================

// Ajuste para o SEU backend no Render:
const API_BASE = "https://gt-jiu-app.onrender.com";

// AVISO IMPORTANTE:
// AS ROTAS ABAIXO SÃO APENAS MODELOS!
// EU VOU AJUSTAR PRA VOCÊ ASSIM QUE ME ENVIAR
// OS ENDPOINTS REAIS QUE APARECEM NO /docs
// =======================================


// =======================================
// LOGIN DO PROFESSOR
// =======================================
async function loginProfessor(email, senha) {
  const resp = await fetch(`${API_BASE}/professor/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, senha }),
  });

  if (!resp.ok) {
    const erro = await resp.text();
    throw new Error("Erro no login do professor: " + erro);
  }

  return resp.json(); // token + dados do professor
}


// =======================================
// LOGIN DO ALUNO
// =======================================
async function loginAluno(codigo, senha) {
  const resp = await fetch(`${API_BASE}/aluno/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ codigo, senha }),
  });

  if (!resp.ok) {
    const erro = await resp.text();
    throw new Error("Erro no login do aluno: " + erro);
  }

  return resp.json(); // token + dados do aluno
}


// =======================================
// BUSCAR MEDALHAS DO ALUNO
// =======================================
async function apiBuscarMedalhasDoAluno(idAluno, token) {
  const resp = await fetch(`${API_BASE}/alunos/${idAluno}/medalhas`, {
    headers: {
      "Authorization": `Bearer ${token}`,
    },
  });

  if (!resp.ok) {
    throw new Error("Erro ao carregar medalhas do aluno");
  }

  return resp.json();
}


// =======================================
// BUSCAR RANKING DO PROFESSOR
// =======================================
async function apiBuscarRanking(idProfessor, token) {
  const resp = await fetch(`${API_BASE}/professores/${idProfessor}/ranking`, {
    headers: {
      "Authorization": `Bearer ${token}`,
    },
  });

  if (!resp.ok) {
    throw new Error("Erro ao buscar ranking");
  }

  return resp.json();
}


// =======================================
// AVISOS
// =======================================
async function apiCriarAviso(titulo, texto, token) {
  const resp = await fetch(`${API_BASE}/avisos`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`,
    },
    body: JSON.stringify({ titulo, texto }),
  });

  if (!resp.ok) {
    throw new Error("Erro ao criar aviso");
  }

  return resp.json();
}

async function apiListarAvisos(idProfessor, token) {
  const resp = await fetch(`${API_BASE}/professores/${idProfessor}/avisos`, {
    headers: { "Authorization": `Bearer ${token}` },
  });

  if (!resp.ok) {
    throw new Error("Erro ao listar avisos");
  }

  return resp.json();
}


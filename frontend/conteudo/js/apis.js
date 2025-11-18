// =======================================
// CONFIGURAÇÃO DO BACKEND (RENDER)
// =======================================

const API_BASE = "https://gt-jiu-app.onrender.com";

// Helper genérico para requisições
async function apiRequest(path, options = {}) {
  const url = `${API_BASE}${path}`;

  const defaultHeaders = {
    "Content-Type": "application/json",
  };

  const resp = await fetch(url, {
    headers: {
      ...defaultHeaders,
      ...(options.headers || {}),
    },
    method: options.method || "GET",
    body: options.body ? JSON.stringify(options.body) : undefined,
  });

  // Tenta parsear JSON; se der errado, retorna texto cru
  const text = await resp.text();
  let data;
  try {
    data = text ? JSON.parse(text) : null;
  } catch {
    data = text;
  }

  if (!resp.ok) {
    const msg =
      (data && data.detail) ||
      (typeof data === "string" ? data : "Erro na requisição à API");
    throw new Error(msg);
  }

  return data;
}

// =======================================
// AUTENTICAÇÃO GENÉRICA
// =======================================

// Registrar usuário (professor / aluno)
// O formato exato depende do backend.
// Aqui vamos mandar APENAS nome, email, senha.
async function apiRegistrarUsuario(dadosUsuario) {
  return apiRequest("/register", {
    method: "POST",
    body: dadosUsuario,
  });
}

// Login genérico
// Exemplo de corpo: { email: "...", senha: "..." }
async function apiLogin(dadosLogin) {
  return apiRequest("/login", {
    method: "POST",
    body: dadosLogin,
  });
}

// =======================================
// AUTENTICAÇÃO ESPECÍFICA - PROFESSOR
// =======================================

// Usado na tela login do professor
async function loginProfessor(email, senha) {
  return apiLogin({
    email: email,
    senha: senha,
    // se o backend NÃO usar role, tudo bem manter só email/senha;
    // se der erro, tiramos esse campo:
    // role: "professor",
  });
}

// Usado na tela de registro do professor
async function registrarProfessor(nome, email, senha) {
  // IMPORTANTE: mandando somente esses 3 campos
  return apiRegistrarUsuario({
    nome: nome,
    email: email,
    senha: senha,
  });
}

// =======================================
// (OPCIONAL) AUTENTICAÇÃO ESPECÍFICA - ALUNO
// =======================================

async function loginAluno(email, senha) {
  return apiLogin({
    email: email,
    senha: senha,
    // role: "aluno",
  });
}

async function registrarAluno(dados) {
  return apiRegistrarUsuario({
    ...dados,
    // role: "aluno",
  });
}

// =======================================
// CATEGORIA (tabela IBJJF/CBJJ)
// =======================================

// Exemplo de corpo: { idade: 27, peso: 76.5, sexo: "masculino" }
async function apiCalcularCategoria(dadosCategoria) {
  return apiRequest("/categoria", {
    method: "POST",
    body: dadosCategoria,
  });
}

// =======================================
// ACADEMIAS
// =======================================

// Criar academia
async function apiCriarAcademia(dadosAcademia) {
  // Exemplo: { nome, mestre, cidade, bairro, endereco, telefone, email, obs }
  return apiRequest("/academias", {
    method: "POST",
    body: dadosAcademia,
  });
}

// Listar academias com filtro opcional
async function apiListarAcademias({ cidade, bairro } = {}) {
  const params = new URLSearchParams();
  if (cidade) params.append("cidade", cidade);
  if (bairro) params.append("bairro", bairro);

  const queryString = params.toString() ? `?${params.toString()}` : "";
  return apiRequest(`/academias${queryString}`, {
    method: "GET",
  });
}

// =======================================
// MEDALHAS
// =======================================

// Criar medalha
async function apiCriarMedalha(dadosMedalha) {
  // Ex.: { aluno_id, academia_id, tipo, categoria, evento, cidade, data }
  return apiRequest("/medalhas", {
    method: "POST",
    body: dadosMedalha,
  });
}

// Listar medalhas
async function apiListarMedalhas(filtros = {}) {
  const params = new URLSearchParams();
  Object.entries(filtros).forEach(([chave, valor]) => {
    if (valor !== undefined && valor !== null && valor !== "") {
      params.append(chave, valor);
    }
  });

  const queryString = params.toString() ? `?${params.toString()}` : "";
  return apiRequest(`/medalhas${queryString}`, {
    method: "GET",
  });
}

// =======================================
// RANKING DE ACADEMIAS
// =======================================

// Ranking geral de academias
async function apiRankingAcademias(filtros = {}) {
  const params = new URLSearchParams();
  Object.entries(filtros).forEach(([chave, valor]) => {
    if (valor !== undefined && valor !== null && valor !== "") {
      params.append(chave, valor);
    }
  });

  const queryString = params.toString() ? `?${params.toString()}` : "";
  return apiRequest(`/ranking/academias${queryString}`, {
    method: "GET",
  });
}

// =======================================
// AVISOS (OPCIONAL - futuro backend)
// =======================================

async function apiCriarAvisoBackend(dadosAviso) {
  return apiRequest("/avisos", {
    method: "POST",
    body: dadosAviso,
  });
}

async function apiListarAvisosBackend(filtros = {}) {
  const params = new URLSearchParams();
  Object.entries(filtros).forEach(([chave, valor]) => {
    if (valor !== undefined && valor !== null && valor !== "") {
      params.append(chave, valor);
    }
  });

  const queryString = params.toString() ? `?${params.toString()}` : "";
  return apiRequest(`/avisos${queryString}`, {
    method: "GET",
  });
}

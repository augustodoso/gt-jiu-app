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
// AUTENTICAÇÃO
// =======================================

// Registrar usuário (ex.: professor ou admin)
// O corpo exato depende do seu backend, aqui deixamos genérico.
async function apiRegistrarUsuario(dadosUsuario) {
  return apiRequest("/register", {
    method: "POST",
    body: dadosUsuario,
  });
}

// Login (pode ser usado tanto para professor quanto para aluno,
// dependendo de como seu backend foi implementado)
async function apiLogin(dadosLogin) {
  // Exemplo esperado: { email: "...", senha: "..." }
  // ou o formato que o seu backend estiver usando
  return apiRequest("/login", {
    method: "POST",
    body: dadosLogin,
  });
}

// =======================================
// CATEGORIA (tabela IBJJF/CBJJ)
// =======================================

// Chama o endpoint /categoria do backend
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

// Criar academia (para quando uma nova academia contratar o app)
async function apiCriarAcademia(dadosAcademia) {
  // Exemplo de corpo: { nome, mestre, cidade, bairro, endereco, telefone, email, obs }
  return apiRequest("/academias", {
    method: "POST",
    body: dadosAcademia,
  });
}

// Listar academias com filtro opcional por cidade/bairro
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

// Criar medalha (aluno envia resultado / professor cadastra)
async function apiCriarMedalha(dadosMedalha) {
  // Ex.: { aluno_id, academia_id, tipo, categoria, evento, cidade, data }
  return apiRequest("/medalhas", {
    method: "POST",
    body: dadosMedalha,
  });
}

// Listar medalhas (pode ter filtros dependendo do backend)
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

// Ranking geral de academias (por medalhas)
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
// (OPCIONAL) AVISOS - se no futuro você criar isso no backend
// =======================================

// Mantive como exemplo caso você crie rotas de avisos depois.
// Por enquanto, o painel está usando localStorage para avisos.

async function apiCriarAvisoBackend(dadosAviso) {
  // Ajuste a rota quando tiver endpoint real
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

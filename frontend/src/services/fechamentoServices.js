import api from "../apis/api";

const obterIndices = () => {
  return api.get("/indices");
};

const obterCryptos = () => {
  return api.get("/cryptos");
};

const obterCurrencies = () => {
  return api.get("/currencies");
};

const obterTodos = () => {
  return api.get("/todos");
};

const consultarFechamentos = (data) => {
  return api.post("/json", data);
};

export default {
  obterIndices,
  obterCryptos,
  obterCurrencies,
  obterTodos,
  consultarFechamentos,
};
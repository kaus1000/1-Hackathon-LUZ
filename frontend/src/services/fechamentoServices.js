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

export default {
  obterIndices,
  obterCryptos,
  obterCurrencies
};
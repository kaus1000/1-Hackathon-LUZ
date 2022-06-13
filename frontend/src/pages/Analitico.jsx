import React, { useState } from "react";
import { toast } from "react-toastify";
import Tabela from "../components/Tabela";
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

// Constantes
import { TABELA_ANALITICO_CABECALHO, OPCOES_SELECT_ANALITICO } from "../constants/analitico/analitico-constants";

// Serviços
import fechamentoServices from "../services/fechamentoServices";

function Analitico() {
  const [itemSelecionado, setItemSelecionado] = useState('');
  const [dadosLista, setDadosLista] = useState([]);

  const msgRetorno = "Não foi possível obter as informações de ";

  // Listar fechamento dos Índices
  const listarIndices = () => {
    fechamentoServices
      .obterIndices()
      .then((resposta) => {
        let data = resposta.data;
        setDadosLista(data);
      })
      .catch((erro) =>
        toast.error(msgRetorno + "índices.")
      );
  };

  // Listar fechamento das Cryptos
  const listarCryptos = () => {
    fechamentoServices
      .obterCryptos()
      .then((resposta) => {
        let data = resposta.data;
        setDadosLista(data);
      })
      .catch((erro) =>
        toast.error(msgRetorno + "cryptos.")
      );
  };

  // Listar fechamento das Currencies
  const listarCurrencies = () => {
    fechamentoServices
      .obterCurrencies()
      .then((resposta) => {
        let data = resposta.data;
        setDadosLista(data);
      })
      .catch((erro) =>
        toast.error(msgRetorno + "currencies.")
      );
  };

  const handleSelecionarItem = (event) => {
    let item = event.target.value;
    setItemSelecionado(item);

    switch (item) {
      case "indices":
        listarIndices();
        break;
      case "cryptos":
        listarCryptos();
        break;
      case "currencies":
        listarCurrencies();
        break;
    }
  };

  return (
    <div className="flex flex-col col-span-full bg-white shadow-lg border border-slate-200">
      <header className="px-5 py-4 border-b border-slate-100 flex items-center">
        <div class="flex">
          <div class="flex-1 w-64">
            <FormControl fullWidth>
              <InputLabel id="select-opcoes-fechamento-label">Fechamento</InputLabel>
              <Select
                labelId="select-opcoes-fechamento-label"
                id="select-opcoes-fechamento"
                value={itemSelecionado}
                label="Fechamento"
                onChange={handleSelecionarItem}
              >
                {OPCOES_SELECT_ANALITICO.map((opcao, index) => (
                  <MenuItem value={opcao.name} key={index}>{opcao.title}</MenuItem>
                ))}
              </Select>
            </FormControl>
          </div>
        </div>
      </header>

      <Tabela colunas={TABELA_ANALITICO_CABECALHO} dados={dadosLista} />
    </div>
  );
}

export default Analitico;

import React, { useState } from "react";
import { toast } from "react-toastify";
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

// Componentes
import Tabela from "../components/Tabela";
import DialogTitle from '@mui/material/DialogTitle';
import Dialog from '@mui/material/Dialog';

// Constantes
import { TABELA_ANALITICO_CABECALHO } from "../constants/analitico/analitico-constants";

// Serviços
import fechamentoServices from "../services/fechamentoServices";

function Analitico() {
  const [carregando, setCarregando] = useState(false);
  const [abrirModal, setAbrirModal] = useState(false);
  const [itemSelecionado, setItemSelecionado] = useState('');
  const [dadosLista, setDadosLista] = useState([]);

  // Lista todos os fechamentos solicitados
  const listarTodos = () => {
    fechamentoServices
      .obterTodos()
      .then((resposta) => {
        let data = resposta.data;
        setDadosLista(data);
      })
      .catch((erro) => toast.error("Não foi possível obter as informações de fechamento."));
  };

  const enviarLista = (data) => {
    setCarregando(true);

    fechamentoServices
      .consultarFechamentos(data)
      .then((resposta) => {
        listarTodos();
        setCarregando(false);
        handleFecharModal();
        toast.success("Consulta realizada com sucesso.");

      })
      .catch((erro) => toast.error("Ocorreu um erro ao realizar a consulta."));
  };

  const handleSelecionarItem = (event) => {
    let item = event.target.value;
    setItemSelecionado(item);
  };

  const handleConsultar = (itens) => {
    let arrayItens = itens.split("\n").filter(item => item.trim());
    let arrayIndices = arrayItens.filter(indice => indice.includes("indices"));
    let arrayCrypto = arrayItens.filter(indice => indice.includes("crypto"));
    let arrayCurrencies = arrayItens.filter(indice => indice.includes("currencies"));

    let data = {
      "indices": Array.isArray(arrayIndices) && arrayIndices.length ? arrayIndices : [],
      "crypto": Array.isArray(arrayCrypto) && arrayCrypto.length ? arrayCrypto : [],
      "currencies": Array.isArray(arrayCurrencies) && arrayCurrencies.length ? arrayCurrencies : [],
    };

    enviarLista(data);
  };

  const handleFecharModal = (value) => {
    setAbrirModal(false);
  };

  return (
    <div className="flex flex-col col-span-full bg-white shadow-lg border border-slate-200">
      <Dialog onClose={handleFecharModal} open={abrirModal}>
        <DialogTitle>Consultar fechamentos</DialogTitle>
        <div className="flex flex-col p-5">
          <div className="flex justify-end" style={{width: "30vw"}}>
            <TextField
              id="item"
              label="Item"
              variant="outlined"
              rows="12"
              onChange={handleSelecionarItem}
              fullWidth
              multiline
            className="grid-cols-12"
            />
          </div>

          <div className="flex justify-end mt-5">
            <Button
              className="btn-padrao-luz"
              variant="contained"
              onClick={() => handleConsultar(itemSelecionado)}
              disabled={!itemSelecionado || carregando}
            >
              { carregando ? 'Consultando...' : 'Consultar' }
            </Button>
          </div>
        </div>
      </Dialog>

      <header className="flex px-5 py-4 border-b border-slate-100">
        <Button className="btn-padrao-luz" variant="contained" onClick={() => setAbrirModal(true)}>Consultar fechamentos</Button>
      </header>

      <Tabela colunas={TABELA_ANALITICO_CABECALHO} dados={dadosLista} />
    </div>
  );
}

export default Analitico;

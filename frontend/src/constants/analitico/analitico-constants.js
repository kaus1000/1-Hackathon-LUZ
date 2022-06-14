const TABELA_ANALITICO_CABECALHO = [
    {
      field: 'tipo',
      headerName: 'Tipo',
      width: 100,
      valueGetter: (params) => {
        let tipo = params.row.tipo;
        return tipo.charAt(0).toUpperCase() + tipo.slice(1)
      }
    },
    {
      field: 'nome',
      headerName: 'Nome',
      width: 500
    },
    {
      field: 'fechamento',
      headerName: 'Fechamento',
      width: 400
    },
];

const OPCOES_SELECT_ANALITICO = [
  {
    name: "indices",
    title: "Índices",
  },
  {
    name: "crypto",
    title: "Cryptos",
  },
  {
    name: "currencies",
    title: "Currencies",
  },
];

export {
  TABELA_ANALITICO_CABECALHO,
  OPCOES_SELECT_ANALITICO,
};
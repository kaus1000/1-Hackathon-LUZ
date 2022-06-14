import * as React from 'react';
import { DataGrid } from '@mui/x-data-grid';

// const columns = [
//   { field: 'id', headerName: 'ID', width: 70 },
//   { field: 'firstName', headerName: 'First name', width: 130 },
//   { field: 'lastName', headerName: 'Last name', width: 130 },
//   {
//     field: 'age',
//     headerName: 'Age',
//     type: 'number',
//     width: 90,
//   },
//   {
//     field: 'fullName',
//     headerName: 'Full name',
//     description: 'This column has a value getter and is not sortable.',
//     sortable: false,
//     width: 160,
//     valueGetter: (params) =>
//       `${params.row.firstName || ''} ${params.row.lastName || ''}`,
//   },
// ];

export default function Tabela(props) {
  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGrid
        rows={props.dados}
        columns={props.colunas}
        pageSize={props.tamanho}
        rowsPerPageOptions={[props.tamanho]}
        checkboxSelection={props.usarCheckbox}
      />
    </div>
  );
}

Tabela.defaultProps = {
  dados: [],
  colunas: [],
  tamanho: 5,
  usarCheckbox: false,
};

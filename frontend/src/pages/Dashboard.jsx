import React from "react";
import FilterButton from "../components/actions/FilterButton";
import Datepicker from "../components/actions/Datepicker";
import DashboardCard from "../components/dashboard/DashboardCard";

function Dashboard() {
  return (
    <>
      <div className="sm:flex sm:justify-end sm:items-center mb-8">
        <div className="grid grid-flow-col sm:auto-cols-max justify-end sm:justify-end gap-2">
          <FilterButton />

          <Datepicker />
        </div>
      </div>

      <div className="grid grid-cols-12 gap-6">
        <DashboardCard titulo="Índices" />

        <DashboardCard titulo="Crypto" />

        <DashboardCard titulo="Currencies" />
      </div>
    </>
  );
}

export default Dashboard;

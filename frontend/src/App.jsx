import React, { useState, useEffect } from "react";
import { Routes, Route, useLocation } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import "./css/style.scss";
import "react-toastify/dist/ReactToastify.css";
import "./charts/ChartjsConfig";

// Componentes
import Sidebar from "./components/Sidebar";
import Header from "./components/Header";

// Páginas
import Dashboard from "./pages/Dashboard";
import Analitico from "./pages/Analitico";

function App(props) {
  const location = useLocation();
  const [sidebarOpen, setSidebarOpen] = useState(false);

  useEffect(() => {
    document.querySelector("html").style.scrollBehavior = "auto";
    window.scroll({ top: 0 });
    document.querySelector("html").style.scrollBehavior = "";
  }, [location.pathname]);

  return (
    <div className="flex h-screen overflow-hidden">
      <Sidebar sidebarOpen={sidebarOpen} setSidebarOpen={setSidebarOpen} />

      <div className="relative flex flex-col flex-1 overflow-y-auto overflow-x-hidden">
        <Header sidebarOpen={sidebarOpen} setSidebarOpen={setSidebarOpen} />

        <main>
          <div className="px-4 sm:px-6 lg:px-8 py-8 w-full max-w-9xl mx-auto">
            <Routes>
              <Route exact path="/" element={<Dashboard />} />
              <Route exact path="/analitico" element={<Analitico />} />
            </Routes>
          </div>

          <ToastContainer />
        </main>
      </div>
    </div>
  );
}

export default App;

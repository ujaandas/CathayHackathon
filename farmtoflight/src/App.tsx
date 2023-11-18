import React from "react";
import { Route, Routes } from "react-router-dom";
import BundleWrapper from "./components/Bundle/BundleWrapper";
import Checkout from "./pages/Checkout";
import Offerings from "./pages/Offerings";

function App() {
  return (
    <Routes>
      <Route path="*" Component={Offerings} />
      <Route path="/bundle" Component={BundleWrapper} />
      <Route path="/new-page" Component={Checkout} />
    </Routes>
  );
}

export default App;

import React from "react";
import Navbar from "../components/Navbar/Navbar";
import BundleWrapper from "../components/Bundle/BundleWrapper";

function Offerings() {
  return (
    <div className="flex flex-col h-screen w-screen bg-gradient-to-t from-white to-[#6db6ae]">
      <Navbar />
      <div className="m-auto">
        <div className="align-middle">
          <BundleWrapper />
        </div>
      </div>
    </div>
  );
}

export default Offerings;

import React, { useState } from "react";
import Overlay from "./Overlay/Overlay";

interface BundleProps {
  title: string;
  description: string[];
  handleSelected: (selected: string) => void;
  selected: string;
}

function Bundle({ title, description, handleSelected, selected }: BundleProps) {
  const [showOverlay, setShowOverlay] = useState(false);

  const handleCustomize = () => {
    setShowOverlay(true);
  };

  const handleCloseOverlay = () => {
    setShowOverlay(false);
  };

  const fruits = ["Apple", "Banana", "Orange", "Pineapple"];

  return (
    <>
      {showOverlay && <Overlay fruits={fruits} onClose={handleCloseOverlay} />}
      <div
        onClick={() => handleSelected(title)}
        className={`mx-5 cursor-pointer align-middle items-center text-center text-black bg-white shadow-xl p-5 rounded-lg transition-all ${
          selected == title ? "bg-sky-600 text-white" : "hover:border-blue-500"
        }`}
      >
        <h1 className="font-extrabold ">{title}</h1>
        {description.map((desc) => (
          <p key={desc} className="bundle-description">
            {desc}
          </p>
        ))}
        <button
          className={`bg-[#006c6f] hover:bg-[#1f4546] text-white p-2 rounded-md mt-5 transition-all ${
            selected == title ? "" : "opacity-0"
          }`}
          onClick={handleCustomize}
        >
          Customize
        </button>
      </div>
    </>
  );
}

export default Bundle;

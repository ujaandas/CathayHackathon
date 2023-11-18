"use client";
import React, { useEffect, useRef, useState } from "react";
import Overlay from "./Overlay";

interface BundleProps {
  title: string;
  description: string[];
}

function Bundle({ title, description }: BundleProps) {
  const [showOverlay, setShowOverlay] = useState(false);
  const [selected, setSelected] = useState(false);
  const newRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleOutsideClick = (e: MouseEvent) => {
      if (newRef.current && !newRef.current.contains(e.target as Node)) {
        setSelected(false);
      }
    };

    document.addEventListener("mousedown", handleOutsideClick);
    return () => {
      document.removeEventListener("mousedown", handleOutsideClick);
    };
  }, []);

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
        onClick={() => setSelected(!selected)}
        className={`mx-5 align-middle items-center text-center text-black bg-white hover:bg-slate-100 shadow-xl p-5 rounded-lg transition-all ${
          selected ? " bg-gradient-to-t from-[#cdedea] to-[#e5eeed]" : ""
        }`}
        ref={newRef}
      >
        <h1 className="font-extrabold ">{title}</h1>
        {description.map((desc) => (
          <p key={desc} className="bundle-description">
            {desc}
          </p>
        ))}
        <button
          className={`bg-[#006c6f] hover:bg-[#1f4546] text-white p-2 rounded-md mt-5 transition-all ${
            selected ? "" : "opacity-0"
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

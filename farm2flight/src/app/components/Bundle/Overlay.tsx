import React from "react";

interface OverlayProps {
  fruits: string[];
  onClose: () => void;
}

function Overlay({ fruits, onClose }: OverlayProps) {
  return (
    <div
      className="fixed top-0 left-0 w-full h-full bg-black bg-opacity-70 flex justify-center items-center z-50"
      onClick={onClose}
    >
      <div className="bg-white p-6 rounded-md">
        <h2 className="text-lg font-semibold mb-4">Fruits:</h2>
        <ul>
          {fruits.map((fruit, index) => (
            <li key={index} className="text-gray-700">
              {fruit}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Overlay;

import React from "react";
import { Link } from "react-router-dom";
import Card from "./Card";
import { ChevronRight } from "react-feather";

interface OverlayProps {
  fruits: string[];
  onClose: () => void;
}

function Overlay({ fruits, onClose }: OverlayProps) {
  return (
    <div
      className="fixed top-0 left-0 w-full h-full bg-black bg-opacity-70 flex justify-center items-center"
      onClick={onClose}
    >
      <div
        className="bg-white p-6 rounded-md z-50 relative"
        onClick={(e) => e.stopPropagation()}
      >
        <h2 className="text-lg font-semibold mb-4">Fruits:</h2>
        <div className="flex flex-row mx-5 my-3">
          {fruits.map((fruit) => (
            <Card
              title={fruit}
              description="wow!!"
              image="https://picsum.photos/50"
              key={fruit}
            />
          ))}
        </div>

        <div className="absolute bottom-3 right-3">
          <Link to="/checkout">
            <ChevronRight size={48} />
          </Link>
        </div>
      </div>
    </div>
  );
}

export default Overlay;

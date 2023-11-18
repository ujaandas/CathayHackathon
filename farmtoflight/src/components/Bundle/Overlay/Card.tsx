import React, { useState } from "react";

interface CardProps {
  title: string;
  description: string;
  image: string;
}

function Card({ title, description, image }: CardProps) {
  const [selected, setSelected] = useState(true);

  return (
    <div
      onClick={() => setSelected(!selected)}
      className={`relative rounded-lg shadow-md overflow-hidden mx-5 my-2 p-3 transition-all`}
    >
      <img className="w-full h-48 object-cover" src={image} alt={title} />
      <div
        className={`absolute inset-0 bg-black bg-opacity-50 ${
          selected ? "hidden" : "block"
        }`}
      ></div>
      <div className={`relative z-10 p-4`}>
        <h2 className="text-xl font-medium text-gray-800 mb-2">{title}</h2>
        <p className="text-sm text-gray-600">{description}</p>
      </div>
    </div>
  );
}

export default Card;

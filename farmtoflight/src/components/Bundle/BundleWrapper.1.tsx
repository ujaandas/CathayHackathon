import React, { useEffect, useState } from "react";
import Bundle from "./Bundle";
import axios from "axios";

export function BundleWrapper() {
  const [selected, setSelected] = useState("");
  const [fruits, setFruits] = useState([]);

  // Fetch fruit data from backend using axios
  useEffect(() => {
    axios
      .get("http://localhost:5000/api/fruits")
      .then((res) => {
        setFruits(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  const bundles = [
    {
      title: "Bundle 1",
      description: ["description 1", "description 2", "description 3"],
    },
    {
      title: "Bundle 2",
      description: ["description 1", "description 2", "description 3"],
    },
    {
      title: "Bundle 3",
      description: ["description 1", "description 2", "description 3"],
    },
    {
      title: "Bundle 4",
      description: ["description 1", "description 2", "description 3"],
    },
    {
      title: "Bundle 5",
      description: ["description 1", "description 2", "description 3"],
    },
  ];

  const handleSelected = (newSelected: string) => {
    console.log(newSelected);
    setSelected(newSelected);
  };

  return (
    <div className="flex flex-row">
      {bundles.map((bundle) => (
        <Bundle
          key={bundle.title}
          title={bundle.title}
          description={bundle.description}
          selected={selected}
          handleSelected={handleSelected}
        />
      ))}
    </div>
  );
}

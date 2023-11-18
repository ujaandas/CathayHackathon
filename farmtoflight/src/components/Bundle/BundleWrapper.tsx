import React, { useEffect, useState } from "react";
import Bundle from "./Bundle";
import axios from "axios";

function BundleWrapper() {
  const [selected, setSelected] = useState("");
  const [fruits, setFruits] = useState([]);

  const bundles = [
    {
      title: "Bundle 1",
      description: [],
    },
    {
      title: "Bundle 2",
      description: [],
    },
    {
      title: "Bundle 3",
      description: [],
    },
    {
      title: "Bundle 4",
      description: [],
    },
  ];
  // Fetch user data from the API

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

export default BundleWrapper;

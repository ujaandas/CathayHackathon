/* eslint-disable @typescript-eslint/no-unused-vars */
import React, { useEffect, useState } from "react";
import Bundle from "./Bundle";
import axios from "axios";

interface BundleWrapperProps {
  user: string;
}

const bundles = [
  {
    title: "The Energizer",
    description: [
      "Oranges and grapefruit give tons of vitamin C",
      "Bananas for quick energy",
      "Apples for fiber and to keep you moving",
      "A small pamphlet with tips on using these fruits to maintain energy",
    ],
  },
  {
    title: "The Weight Management Kit",
    description: [
      "Berries like strawberries, blueberries and raspberries",
      "Pears and peaches for healthy bowel movement",
      "Grapefruit as a metabolism booster",
      "A short guide on how to incorporate these fruits into your diet",
    ],
  },
  {
    title: "The Tokyo Collection",
    description: [
      "Asian pears, persimmons, and yuzu",
      "Melons, especially varieties popular in Japan like the infamous Musk Melon",
      "Packets of dried umeboshi for a savory option",
      "An insert explaining the role of these fruits in Japanese cuisine",
    ],
  },
  {
    title: "The Antioxidant Assortment",
    description: [
      "Dark berries (blueberries, blackberries)",
      "Red grapes and pomegranates",
      "Kiwis and cherries",
      "Educational material on antioxidants and their health benefits",
    ],
  },
  {
    title: "The Sweet Treat Box",
    description: [
      "Dried fruits like dates, figs, and raisins",
      "Sweet fresh fruits like pineapples, melons, and mangoes",
      "A recipe card for making healthy fruit-based desserts",
    ],
  },
];

function BundleWrapper({ user }: BundleWrapperProps) {
  const [selected, setSelected] = useState("");

  const handleSelected = (newSelected: string) => {
    console.log(newSelected);
    setSelected(newSelected);
  };

  return (
    <div className="text-center">
      <h1 className="font-extrabold text-4xl mb-10">
        Recommendations for you:
      </h1>
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
    </div>
  );
}

export default BundleWrapper;

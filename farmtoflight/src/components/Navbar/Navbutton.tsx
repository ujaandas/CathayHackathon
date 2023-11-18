import React from "react";

interface NavbuttonProps {
  name: string;
  href: string;
  children: React.ReactNode; // Icon goes here
}

function Navbutton({ name, href, children }: NavbuttonProps) {
  return (
    <a href={href}>
      <div className="flex-col hover:bg-gray-200 hover:font-bold p-3 rounded-md transition-all">
        <div className="flex items-center justify-center">{children}</div>
        <div>{name}</div>
      </div>
    </a>
  );
}

export default Navbutton;

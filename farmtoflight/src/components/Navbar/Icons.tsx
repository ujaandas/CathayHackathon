import React from "react";
import Navbutton from "./Navbutton";
import { Home } from "react-feather";

function Icons() {
  const navitems = [
    { name: "Farm2Flight", href: "/", icon: <Home /> },
    { name: "Cathay Shop", href: "/", icon: <Home /> },
    { name: "Featured", href: "/", icon: <Home /> },
    { name: "Home", href: "/", icon: <Home /> },
    { name: "Wellness", href: "/", icon: <Home /> },
    { name: "Food & Wine", href: "/", icon: <Home /> },
    { name: "Electronics", href: "/", icon: <Home /> },
    { name: "Fashion & Beauty", href: "/", icon: <Home /> },
    { name: "Travel", href: "/", icon: <Home /> },
    { name: "Exclusives", href: "/", icon: <Home /> },
  ];

  const navbuttons = navitems.map((navitem) => (
    <Navbutton key={navitem.name} name={navitem.name} href={navitem.href}>
      {navitem.icon}
    </Navbutton>
  ));

  return (
    <nav className="bg-slate-100 mx-auto items-center px-10 py-2 w-full shadow-sm">
      <div className="flex justify-between space-x-4">{navbuttons}</div>
    </nav>
  );
}

export default Icons;

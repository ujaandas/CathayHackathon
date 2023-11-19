import React from "react";
import Navbutton from "./Navbutton";
import {
  Home,
  Compass,
  Gift,
  BatteryCharging,
  Trello,
  User,
  Activity,
  ShoppingBag,
  Feather,
  DollarSign,
} from "react-feather";

function Icons() {
  const navitems = [
    { name: "Farm2Flight", href: "/", icon: <Feather /> },
    { name: "Cathay Shop", href: "/", icon: <ShoppingBag /> },
    { name: "Featured", href: "/", icon: <Activity /> },
    { name: "Home", href: "/", icon: <Home /> },
    { name: "Wellness", href: "/", icon: <User /> },
    { name: "Food & Wine", href: "/", icon: <Trello /> },
    { name: "Electronics", href: "/", icon: <BatteryCharging /> },
    { name: "Fashion & Beauty", href: "/", icon: <Gift /> },
    { name: "Travel", href: "/", icon: <Compass /> },
    { name: "Exclusives", href: "/", icon: <DollarSign /> },
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

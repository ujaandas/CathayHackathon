/* eslint-disable @typescript-eslint/no-unused-vars */
import React, { useEffect, useState } from "react";
import Icons from "./Icons";
import axios from "axios";

interface NavbarProps {
  user: string;
}

function Navbar({ user }: NavbarProps) {
  return (
    <>
      <div className="flex-row bg-slate-200 px-20 py-2 justify-between items-center shadow-xl">
        <div className="flex items-center">
          <div className="justify-start flex-grow">
            <img
              src="/logo.png"
              alt="Farm2Flight Logo"
              width={40}
              height={40}
            />
          </div>
          <div>
            <h3 className="text-l font-bold">{`Welcome, ${user}!`}</h3>
          </div>
          <div className="flex flex-row justify-end">
            <h3 className="text-xl font-extrabold ml-4">Farm2Flight</h3>
          </div>
        </div>
      </div>
      <Icons />
    </>
  );
}

export default Navbar;

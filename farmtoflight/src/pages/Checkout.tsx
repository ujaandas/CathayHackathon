import React from "react";
import Navbar from "../components/Navbar/Navbar";

interface CheckoutProps {
  user: string;
}
function Checkout({ user }: CheckoutProps) {
  return (
    <div>
      <Navbar user={user} />
      <div className="flex flex-row justify-end mr-10">
        <div className="text-align align-middle items-center">
          <img src="plane.webp" width={500} height={50}></img>
          <h2 className="font-bold text-2xl text-center">
            {" "}
            {`Your product will arrive in ${Math.round(
              Math.random() * (8 - 1) + 1
            )} days!`}
          </h2>
        </div>
        <img src="reciept.png" width={650} height={650}></img>
      </div>
    </div>
  );
}

export default Checkout;

import React from "react";
import Navbar from "../components/Navbar/Navbar";

interface CheckoutProps {
  user: string;
}
function Checkout({ user }: CheckoutProps) {
  return (
    <div>
      <Navbar user={user} />
      <div className="flex flex-row justify-end">
        <img src="reciept.png" width={650} height={650}></img>
      </div>
    </div>
  );
}

export default Checkout;

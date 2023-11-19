import { Route, Routes } from "react-router-dom";
import Checkout from "./pages/Checkout";
import Offerings from "./pages/Offerings";
import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  // GET user from backend via axios
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const [user, setUser] = useState<string>("");

  useEffect(() => {
    axios
      .get("http://localhost:8000/getUser")
      .then((res) => {
        setUser(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);
  return (
    <Routes>
      <Route path="*" element={<Offerings user={user} />} />
      <Route path="/checkout" element={<Checkout user={user} />} />
    </Routes>
  );
}

export default App;

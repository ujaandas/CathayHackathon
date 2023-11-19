import Navbar from "../components/Navbar/Navbar";
import BundleWrapper from "../components/Bundle/BundleWrapper";

interface OfferingsProps {
  user: string;
}

function Offerings({ user }: OfferingsProps) {
  return (
    <div className="flex flex-col h-screen w-screen bg-gradient-to-t from-white to-[#6db6ae]">
      <Navbar user={user} />
      <div className="m-auto">
        <div className="align-middle">
          <BundleWrapper user={user} />
        </div>
      </div>
    </div>
  );
}

export default Offerings;

import Bundle from "./components/Bundle/Bundle";
import Navbar from "./components/Navbar/Navbar";

function Home() {
  const bundles = [
    {
      title: "Bundle 1",
      description: ["description 1", "description 2", "description 3"],
    },
    {
      title: "Bundle 2",
      description: ["description 1", "description 2", "description 3"],
    },
    {
      title: "Bundle 3",
      description: ["description 1", "description 2", "description 3"],
    },
    {
      title: "Bundle 4",
      description: ["description 1", "description 2", "description 3"],
    },
    {
      title: "Bundle 5",
      description: ["description 1", "description 2", "description 3"],
    },
  ];
  return (
    <main className="flex flex-col h-screen w-screen bg-gradient-to-t from-white to-[#6db6ae] ">
      <Navbar />
      <div className="m-auto">
        <div className="align-middle">
          <div className="flex flex-row">
            {bundles.map((bundle) => (
              <Bundle
                key={bundle.title}
                title={bundle.title}
                description={bundle.description}
              />
            ))}
          </div>
        </div>
      </div>
    </main>
  );
}

export default Home;

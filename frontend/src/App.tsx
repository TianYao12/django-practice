import { useState, useEffect, ChangeEvent, FormEvent } from "react";
import "./App.css";

interface Data {
  id: number;
  title: string;
  description: string;
  demo_link: string;
  source_link: string;
  created: string;
}

interface FormData {
  title: string;
  description: string;
  demo_link: string;
  source_link: string;
}

function App() {
  const [data, setData] = useState<Data[] | null>(null);
  const [formData, setFormData] = useState<FormData>({
    title: "",
    description: "",
    demo_link: "",
    source_link: "",
  });

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(
          `${import.meta.env.VITE_API_URL}projects/`
        );
        if (!response.ok) {
          throw new Error("Network response error");
        }
        const data = await response.json();
        console.log("data", data);
        setData(data);
      } catch (error) {
        console.error("Error fetching data", error);
      }
      console.log(import.meta.env.VITE_API_URL);
    };
    fetchData();
  }, []);

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL}projects/`, {
        method: "POST",
        headers: { "Content-type": "application/json" },
        body: JSON.stringify(formData),
      });
      if (!response.ok) {
        console.log("Error with response");
      }
      const newData: Data = await response.json();
      setData((prevData) => [...(prevData || []), newData]);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <>
      <div>
        <p>hello world</p>
      </div>
      {data ? (
        <div>
          {data.map((project) => (
            <>
              <p>id: {project.id}</p>
              <p>Title: {project.title}</p>
              <p>Description: {project.description}</p>
              <p>Demo Link: {project.demo_link}</p>
              <p>Source Link: {project.source_link}</p>
              <p>Created: {project.created}</p>
            </>
          ))}
        </div>
      ) : (
        <div>Loading...</div>
      )}
      <div>
        <h2>Add New Project</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            name="title"
            placeholder="Title"
            value={formData.title}
            onChange={handleChange}
          />
          <input
            type="text"
            name="description"
            placeholder="Description"
            value={formData.description}
            onChange={handleChange}
          />
          <input
            type="text"
            name="demo_link"
            placeholder="Demo Link"
            value={formData.demo_link}
            onChange={handleChange}
          />
          <input
            type="text"
            name="source_link"
            placeholder="Source Link"
            value={formData.source_link}
            onChange={handleChange}
          />
          <button type="submit">Submit</button>
        </form>
      </div>
    </>
  );
}

export default App;

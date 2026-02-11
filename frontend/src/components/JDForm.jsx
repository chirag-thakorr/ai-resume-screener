import { useState } from "react";
import { api } from "../api/api";

export default function JDForm({ onCreated }) {
  const [title, setTitle] = useState("");
  const [text, setText] = useState("");

  const submit = async () => {
    const res = await api.post("jd/create/", { title, text });
    onCreated(res.data.id);
  };

  return (
    <div>
      <h3>Create JD</h3>
      <input placeholder="Title" onChange={e=>setTitle(e.target.value)} />
      <textarea placeholder="JD text" onChange={e=>setText(e.target.value)} />
      <button onClick={submit}>Create JD</button>
    </div>
  );
}

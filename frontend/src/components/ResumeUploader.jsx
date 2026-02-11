import { useState } from "react";
import { api } from "../api/api";

export default function ResumeUploader() {
  const [file, setFile] = useState(null);
  const [msg, setMsg] = useState("");

  const upload = async () => {
    const form = new FormData();
    form.append("file", file);

    const res = await api.post("upload/", form);
    setMsg("Uploaded: " + res.data.name);
  };

  return (
    <div>
      <h3>Upload Resume</h3>
      <input type="file" onChange={e => setFile(e.target.files[0])}/>
      <button onClick={upload}>Upload</button>
      <p>{msg}</p>
    </div>
  );
}

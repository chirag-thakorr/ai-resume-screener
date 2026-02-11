import { useState } from "react";
import ResumeUploader from "../components/ResumeUploader";
import JDForm from "../components/JDForm";
import MatchResults from "./MatchResults";

export default function Dashboard() {
  const [jdId, setJdId] = useState(null);

  return (
    <div>
      <h2>AI Resume Screener</h2>

      <ResumeUploader />

      <JDForm onCreated={setJdId} />

      {jdId && <MatchResults jdId={jdId} />}
    </div>
  );
}

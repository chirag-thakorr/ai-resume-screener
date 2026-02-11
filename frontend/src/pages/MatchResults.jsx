import { useState } from "react";
import { api } from "../api/api";
import ResultsTable from "../components/ResultsTable";

export default function MatchResults({ jdId }) {
  const [data, setData] = useState([]);

  const load = async () => {
    const res = await api.get(`match/${jdId}/`);
    setData(res.data);
  };

  return (
    <div>
      <button onClick={load}>Run Matching</button>
      <ResultsTable data={data} />
    </div>
  );
}

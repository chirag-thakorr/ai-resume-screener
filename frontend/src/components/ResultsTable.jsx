export default function ResultsTable({ data }) {

  if (!data || data.length === 0) {
    return <p>No matches found</p>;
  }

  return (
    <table border="1">
      <thead>
        <tr>
          <th>Name</th>
          <th>Final Score</th>
          <th>Semantic</th>
          <th>Skills</th>
        </tr>
      </thead>

      <tbody>
        {data.map(r => (
          <tr key={r.resume_id}>
            <td>{r.name}</td>
            <td>{r.final_score}</td>
            <td>{r.semantic_score}</td>
            <td>{r.matched_skills.join(", ")}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

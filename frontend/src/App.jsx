import { useState } from "react";

function App() {
  const [csvFile, setCsvFile] = useState(null);
const [resumeFile, setResumeFile] = useState(null);
const [githubUrl, setGithubUrl] = useState("");

  return (
    <div
      style={{
        maxWidth: "900px",
        margin: "40px auto",
        padding: "20px",
        fontFamily: "Arial",
      }}
    >
      <h1>Candidate Profile Transformer</h1>

      <p>
        Merge Recruiter CSV + GitHub + Resume Text into one canonical profile.
      </p>

      <hr />
 
      <h3>Recruiter CSV</h3>

        <input
              type="file"
              accept=".csv"
              onChange={(e) => setCsvFile(e.target.files[0])}
        />
      <br />
      <br />

      <h3>GitHub Profile URL</h3>
      <input
        type="text"
        placeholder="https://github.com/username"
        value={githubUrl}
        onChange={(e) => setGithubUrl(e.target.value)}
        style={{
          width: "100%",
          padding: "10px",
        }}
      />

      <br />
      <br />

      <h3>Resume / CV</h3>

      <input
         type="file"
         accept=".pdf,.doc,.docx,.txt"
         onChange={(e) => setResumeFile(e.target.files[0])}
      />

      <br />
      <br />

      <h3>Output Configuration</h3>

      <select>
        <option>Default</option>
        <option>Compact</option>
      </select>

      <br />
      <br />

      <button
        style={{
          padding: "12px 24px",
          cursor: "pointer",
        }}
      >
        Transform Candidate
      </button>

      <hr />

      <h2>Output</h2>

      <pre
        style={{
          background: "#f4f4f4",
          padding: "20px",
          borderRadius: "10px",
        }}
      >
{`{
  "full_name": "John Doe",
  "skills": ["Python", "React", "SQL"]
}`}
      </pre>
    </div>
  );
}

export default App;
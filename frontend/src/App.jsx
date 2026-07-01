import { useState } from "react";
import { transformCandidate } from "./services/api.js";

function App() {
  const [csvFile, setCsvFile] = useState(null);
const [resumeFile, setResumeFile] = useState(null);
const [githubUrl, setGithubUrl] = useState("");
const [result, setResult] = useState(null);
const [loading, setLoading] = useState(false);
const [projection, setProjection] =useState("default");
const [projectionFile, setProjectionFile] =useState(null);

  const handleTransform = async () => {
  if (!csvFile && !resumeFile && !githubUrl.trim()) {
  alert("Please provide at least one source!");
  return;
   }

  try {
    setLoading(true);

    const data = await transformCandidate(
      csvFile,
      resumeFile,
      githubUrl,
      projection,
      projectionFile
    );

    setResult(data);

  } catch (error) {
    console.error(error);
    alert("Transformation failed!");

  } finally {
    setLoading(false);
  }
};
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
        Merge Recruiter CSV + GitHub + Resume into one canonical profile.
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

       <select
            value={projection}
            onChange={(e) => setProjection(e.target.value)}
       >
            <option value="default">Default</option>
            <option value="compact">Compact</option>
            <option value="recruiter">Recruiter</option>
            <option value="engineering">Engineering</option>
            <option value="custom">Custom Projection Config</option>
        </select>

      <br />
     <br />

{projection === "custom" && (
  <>
    <h4>Upload Projection JSON</h4>

    <input
      type="file"
      accept=".json"
      onChange={(e) =>
        setProjectionFile(e.target.files[0])
      }
    />

    <p style={{ color: "gray", fontSize: "14px" }}>
Example JSON:
{`
{
  "fields": [
    {
      "path": "candidate_name",
      "from": "full_name",
      "type": "string"
    },
    {
      "path": "tech_stack",
      "from": "skills",
      "type": "array"
    }
  ],
  "include_confidence": true,
  "include_provenance": false,
  "on_missing": "null"
}
`}
</p>
  </>
)}
      <br></br>

      <button onClick={handleTransform}>
  {loading ? "Transforming..." : "Transform Candidate"}
</button>

      <hr />

      <h2>Output</h2>

      <pre>
  {result
    ? JSON.stringify(result, null, 2)
    : "No transformation yet."}
</pre>
    </div>
  );
}

export default App;
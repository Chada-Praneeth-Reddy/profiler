import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

export const transformCandidate = async (
  csvFile,
  resumeFile,
  githubUrl
) => {
  const formData = new FormData();
  
   if (csvFile) {
  formData.append("csv_file", csvFile);
}

if (resumeFile) {
  formData.append("resume_file", resumeFile);
}

if (githubUrl.trim()) {
  formData.append("github_url", githubUrl.trim());
}

  const response = await axios.post(
    `${API_BASE_URL}/transform`,
    formData
  );

  return response.data;
};
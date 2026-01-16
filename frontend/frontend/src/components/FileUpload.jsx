import { useState } from "react";
import { uploadPDF } from "../api";

function FileUpload() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  const handleUpload = async () => {
    if (!file) return;

    setStatus("Uploading...");
    const res = await uploadPDF(file);
    setStatus(res.message || "Uploaded");
  };

  return (
    <div>
      <h3>Upload PDF</h3>
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <br /><br />
      <button onClick={handleUpload}>Upload</button>
      <p>{status}</p>
    </div>
  );
}

export default FileUpload;

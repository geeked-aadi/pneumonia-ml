import { useState } from "react";

function App() {
    const [file, setFile] = useState(null);
    const [preview, setPreview] = useState(null);
    const [result, setResult] = useState(null);

    const handleUpload = (e) => {
        const selected = e.target.files[0];

        setFile(selected);

        setPreview(
            URL.createObjectURL(selected)
        );
    };

    const analyzeImage = async () => {
        const formData = new FormData();

        formData.append("file", file);

        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        setResult(data);
    };

    return (
        <div style={{ padding: "30px" }}>
        <h1>Pneumonia Detection AI</h1>

        <input
        type="file"
        accept="image/*"
        onChange={handleUpload}
        />

        {preview && (
            <>
            <img
            src={preview}
            alt="preview"
            width="400"
            />

            <br />

            <button
            onClick={analyzeImage}
            >
            Analyze
            </button>
            </>
        )}

        {result && (
            <div>
            <h2>
            Prediction:
            {" "}
            {result.prediction}
            </h2>

            <h3>
            Confidence:
            {" "}
            {result.confidence.toFixed(2)}%
            </h3>
            </div>
        )}
        </div>
    );
}

export default App;

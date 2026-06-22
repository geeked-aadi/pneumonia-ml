import { useState } from "react";

function App() {
    const [file, setFile] = useState(null);
    const [preview, setPreview] = useState(null);
    const [result, setResult] = useState(null);

    const handleUpload = (e) => {
        const selected = e.target.files[0];

        if (!selected) return;

        setFile(selected);
        setPreview(URL.createObjectURL(selected));
        setResult(null);
    };

    const analyzeImage = async () => {
        if (!file) return;

        const formData = new FormData();
        formData.append("file", file);

        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",
                body: formData,
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
            <div style={{ marginTop: "20px" }}>
            <img
            src={preview}
            alt="preview"
            width="350"
            />
            </div>

            <br />

            <button onClick={analyzeImage}>
            Analyze
            </button>
            </>
        )}

        {result && (
            <>
            <div style={{ marginTop: "30px" }}>
            <h2>
            Prediction: {result.prediction}
            </h2>

            <h3>
            Confidence: {result.confidence}%
            </h3>

            <h3>
            Risk: {result.risk}
            </h3>
            </div>

            <div
            style={{
                display: "flex",
                gap: "20px",
                marginTop: "30px",
            }}
            >
            <div>
            <h3>Original X-Ray</h3>

            <img
            src={preview}
            alt="original"
            width="350"
            />
            </div>

            <div>
            <h3>Grad-CAM</h3>

            <img
            src={`${result.heatmap}?t=${Date.now()}`}
            alt="gradcam"
            width="350"
            />
            </div>
            </div>

            {result.prediction === "PNEUMONIA" && (
                <div style={{ marginTop: "30px" }}>
                <h2>About Pneumonia</h2>

                <p>
                Pneumonia is an infection that inflames
                the air sacs in one or both lungs.
                </p>

                <h3>Symptoms</h3>
                <ul>
                <li>Cough</li>
                <li>Fever</li>
                <li>Chest Pain</li>
                <li>Difficulty Breathing</li>
                </ul>

                <h3>Prevention</h3>
                <ul>
                <li>Vaccination</li>
                <li>Hand Hygiene</li>
                <li>Avoid Smoking</li>
                </ul>
                </div>
            )}
            </>
        )}
        </div>
    );
}

export default App;

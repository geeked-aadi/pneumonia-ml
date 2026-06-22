import { useState } from "react";

export default function App() {
    const [image, setImage] = useState(null);

    const handleUpload = (e) => {
        const file = e.target.files[0];

        if (file) {
            setImage(URL.createObjectURL(file));
        }
    };

    return (
        <div className="min-h-screen p-10">
        <h1 className="text-4xl font-bold mb-8">
        Pneumonia Detection AI
        </h1>

        <input
        type="file"
        accept="image/*"
        onChange={handleUpload}
        />

        {image && (
            <img
            src={image}
            alt="uploaded"
            className="w-96 mt-6 rounded-xl"
            />
        )}
        </div>
    );
}

from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io

from predict import predict_image

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "running"
    }

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):

    contents = await file.read()

    image = Image.open(
        io.BytesIO(contents)
    ).convert("RGB")

    result = predict_image(image)

    return result

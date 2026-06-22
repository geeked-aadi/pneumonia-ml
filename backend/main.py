from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io
from fastapi.middleware.cors import CORSMiddleware

from predict import predict_image

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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

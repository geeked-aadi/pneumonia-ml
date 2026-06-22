from PIL import Image
from torchvision import transforms
import torch

from model_loader import model
from gradcam import generate_gradcam

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

classes = [
    "NORMAL",
    "PNEUMONIA"
]

def predict_image(image_pil):

    image = transform(image_pil)

    image = image.unsqueeze(0)

    with torch.no_grad():

        outputs = model(image)

        probs = torch.softmax(outputs, dim=1)

        pred = probs.argmax(dim=1).item()

    confidence = probs[0][pred].item() * 100

    if confidence >= 90:
        risk = "HIGH"
    elif confidence >= 70:
        risk = "MEDIUM"
    else:
        risk = "LOW"
    heatmap_path = generate_gradcam(
    image_pil
)

    return {
    "prediction": classes[pred],
    "confidence": round(confidence, 2),
    "risk": risk,
    "heatmap": "http://127.0.0.1:8000/heatmaps/latest_heatmap.png"
}

from PIL import Image
from torchvision import transforms
import torch

from model_loader import model

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

classes = [
    "NORMAL",
    "PNEUMONIA"
]

def predict_image(image):

    image = transform(image)

    image = image.unsqueeze(0)

    with torch.no_grad():

        outputs = model(image)

        probs = torch.softmax(outputs, dim=1)

        pred = probs.argmax(dim=1).item()

    return {
        "prediction": classes[pred],
        "confidence": float(
            probs[0][pred] * 100
        )
    }

import os
import cv2
import numpy as np
import torch

from PIL import Image

from torchvision import transforms

from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image
from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget

from model_loader import model

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def generate_gradcam(image):

    # Enable gradients
    for param in model.features.parameters():
        param.requires_grad = True

    input_tensor = transform(image)
    input_tensor = input_tensor.unsqueeze(0)

    output = model(input_tensor)

    pred_class = output.argmax(dim=1).item()

    target_layers = [model.features[7][0]]

    cam = GradCAM(
        model=model,
        target_layers=target_layers
    )

    targets = [
        ClassifierOutputTarget(pred_class)
    ]

    grayscale_cam = cam(
        input_tensor=input_tensor,
        targets=targets
    )[0]

    rgb_img = np.array(
        image.resize((224, 224))
    ).astype(np.float32) / 255.0

    visualization = show_cam_on_image(
        rgb_img,
        grayscale_cam,
        use_rgb=True
    )

    os.makedirs("heatmaps", exist_ok=True)

    filename = "heatmaps/latest_heatmap.png"

    cv2.imwrite(
        filename,
        cv2.cvtColor(
            visualization,
            cv2.COLOR_RGB2BGR
        )
    )

    return filename

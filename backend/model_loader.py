from huggingface_hub import hf_hub_download

import torch
import torch.nn as nn
from torchvision.models import efficientnet_b0

model_path = hf_hub_download(
    repo_id="rickGrimes67/pneumonia",
    filename="pneumonia_model.pth"
)

model = efficientnet_b0(weights=None)

model.classifier[1] = nn.Linear(
    model.classifier[1].in_features,
    2
)

model.load_state_dict(
    torch.load(model_path, map_location="cpu")
)

model.eval()

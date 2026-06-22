from PIL import Image

from gradcam import generate_gradcam

img = Image.open("/home/matt/Downloads/pneu.jpeg").convert("RGB")

path = generate_gradcam(img)

print(path)

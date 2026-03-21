import torch
from PIL import Image
from torchvision import transforms
from model import get_model

model = get_model()
model.load_state_dict(torch.load("model.pth"))
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def predict(img_path):
    img = Image.open(img_path).convert("RGB")
    img = transform(img).unsqueeze(0)

    output = model(img)
    _, pred = torch.max(output, 1)

    return "Defect" if pred.item() == 1 else "Normal"
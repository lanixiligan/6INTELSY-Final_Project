import torch.nn as nn
import torchvision.models as models

def get_model():
    model = models.resnet18(pretrained=True)
    model.fc = nn.Linear(512, 2)
    return model
import torch
import torch.nn as nn
import torch.optim as optim
from model import get_model
from dataset import get_loaders

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

train_loader, _ = get_loaders("data/mvtec/bottle")

model = get_model().to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(2):
    total_loss = 0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        outputs = model(images)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1}: {total_loss:.4f}")

torch.save(model.state_dict(), "model.pth")
import torch
import torch.optim as optim
from src.dataset import get_dataloaders
from src.model import BottleCNN
from sklearn.linear_model import LogisticRegression
import os

def train():
    os.makedirs("experiments/logs", exist_ok=True)
    # Correct path based on your folder structure
    data_path = "data/mvtec/bottle" 
    
    if not os.path.exists(data_path):
        print(f"❌ Error: {data_path} not found. Check your manual download.")
        return

    train_loader, val_loader = get_dataloaders(data_path)

    # --- Baseline ---
    imgs, labels = next(iter(train_loader))
    X_flat = imgs.view(imgs.size(0), -1).numpy()
    clf = LogisticRegression(max_iter=50).fit(X_flat, labels.numpy())
    acc = clf.score(X_flat, labels.numpy())
    with open("experiments/logs/baseline_results.txt", "w") as f:
        f.write(f"Simple ML Baseline Accuracy: {acc:.4f}")

    # --- CNN ---
    model = BottleCNN()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = torch.nn.CrossEntropyLoss()

    print("Training Bottle CNN...")
    model.train()
    for images, labels in train_loader:
        optimizer.zero_grad()
        loss = criterion(model(images), labels)
        loss.backward()
        optimizer.step()
    
    torch.save(model.state_dict(), "model.pth")
    print("✅ model.pth saved and metrics logged.")

if __name__ == "__main__":
    train()
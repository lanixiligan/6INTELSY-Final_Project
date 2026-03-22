import os
import glob
from PIL import Image
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from sklearn.model_selection import train_test_split

class BottleDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.image_paths = []
        self.labels = []

        # 1. Collect GOOD images (Label 0)
        train_good = glob.glob(os.path.join(root_dir, "train", "good", "*.png"))
        test_good = glob.glob(os.path.join(root_dir, "test", "good", "*.png"))
        for p in train_good + test_good:
            self.image_paths.append(p)
            self.labels.append(0)

        # 2. Collect DEFECTIVE images (Label 1)
        test_path = os.path.join(root_dir, "test")
        if os.path.exists(test_path):
            defect_folders = [d for d in os.listdir(test_path) if d != "good"]
            for folder in defect_folders:
                paths = glob.glob(os.path.join(test_path, folder, "*.png"))
                for p in paths:
                    self.image_paths.append(p)
                    self.labels.append(1)

    def __len__(self): return len(self.image_paths)

    def __getitem__(self, idx):
        image = Image.open(self.image_paths[idx]).convert("RGB")
        if self.transform: image = self.transform(image)
        return image, self.labels[idx]

def get_dataloaders(root_dir, batch_size=16):
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    dataset = BottleDataset(root_dir, transform=transform)
    train_idx, val_idx = train_test_split(range(len(dataset)), test_size=0.2, stratify=dataset.labels, random_state=42)
    
    train_loader = DataLoader(torch.utils.data.Subset(dataset, train_idx), batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(torch.utils.data.Subset(dataset, val_idx), batch_size=batch_size)
    return train_loader, val_loader
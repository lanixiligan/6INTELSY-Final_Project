import torch
from torch.utils.data import DataLoader, TensorDataset

def get_loaders(_):
    # Create fake images (100 samples, 3x224x224)
    X = torch.randn(100, 3, 224, 224)

    # Fake labels (0 or 1)
    y = torch.randint(0, 2, (100,))

    dataset = TensorDataset(X, y)

    loader = DataLoader(dataset, batch_size=8, shuffle=True)

    return loader, loader
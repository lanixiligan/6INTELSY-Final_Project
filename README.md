# Manufacturing Defect Detection using CNN

# Group Members
- Iligan, Lanix 
- Wylengco, Teyshaun Zell
- Bongon, Joshwell
- Sampang, Denzel

## Description
This project builds a CNN-based system for detecting manufacturing defects using industrial images.

The system includes:
- CNN for defect classification
- Grad-CAM for explainability
- NLP module for defect guidance
- Reinforcement Learning threshold tuner

## Dataset
MVTec Anomaly Detection Dataset

## 🚀 Quick Start (Windows)
1. **Data Setup:** - Download the Bottle dataset from [Kaggle](https://www.kaggle.com/datasets/ipythonx/mvtec-ad).
   - Extract it to `data/mvtec/bottle/` such that `train/` and `test/` are directly inside.
2. **Execution:**
   - Double-click `run.bat` or run `python -m src.train` in your terminal.

## 📂 Project Structure
* `src/`: Core logic (CNN, RL Agent, NLP Reporter, Dataset Loader).
* `data/`: Local storage for MVTec images (Excluded from Git).
* `experiments/`: Auto-generated logs, model weights (`model.pth`), and RL curves.
* `notebooks/`: EDA and visualization of defects.
* `docs/`: Project reports and ethics statements.

## 🛠️ Components
- **CNN:** A custom PyTorch model for binary classification (Good vs. Defective).
- **RL Agent:** Optimizes the decision threshold to minimize "Missed Defect" costs.
- **NLP:** Automatically generates industrial maintenance logs based on model output.

## 📊 Status: Week 2 Checkpoint
- [x] Data Pipeline verified with custom MVTec loader.
- [x] CNN Model training successfully and saving weights.
- [x] Baseline metrics established and logged.
- [x] RL and NLP scaffolds functional.
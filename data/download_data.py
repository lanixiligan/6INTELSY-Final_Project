import os

def main():
    print("="*50)
    print(" 🛠️ MVTec Dataset Manual Setup Guide ")
    print("="*50)

    print("\n1. Download 'bottle' (or full set) from Kaggle:")
    print("   https://www.kaggle.com/datasets/ipythonx/mvtec-ad")

    print("\n2. Extract the folder into your project so the path is:")
    print("   data/mvtec/bottle/train/good/")
    print("   data/mvtec/bottle/test/broken_large/ (etc.)")

    print("\n3. NOTE: You do NOT need to move files.")
    print("   The src/dataset.py script handles the labeling automatically.")

    print("\n" + "="*50)

    if os.path.exists("data/mvtec/bottle"):
        print("\n✅ Path detected! You are ready to run 'bash run.sh'.")
    else:
        print("\n⚠️ Path 'data/mvtec/bottle' not found yet.")

if __name__ == "__main__":
    main()
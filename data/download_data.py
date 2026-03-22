import os

def main():
    print("="*50)
    print(" MVTec Dataset Setup Guide ")
    print("="*50)

    print("\nStep 1: Download the dataset manually from Kaggle:")
    print("https://www.kaggle.com/datasets/ipythonx/mvtec-ad")

    print("\nStep 2: Move the downloaded ZIP file into:")
    print("project-root/data/")

    print("\nStep 3: Extract the ZIP file inside the data/ folder")

    print("\nStep 4: Rename the extracted folder to 'mvtec'")
    print("Expected path: data/mvtec/")

    print("\nStep 5: Ensure the structure looks like this:")
    print("data/mvtec/bottle/train/good/")
    print("data/mvtec/bottle/test/")

    print("\nStep 6 (IMPORTANT):")
    print("Create a 'defect' folder inside train/ and copy some defect images into it.")
    print("Example:")
    print("data/mvtec/bottle/train/defect/")

    print("\n" + "="*50)

    # Ask user for confirmation
    answer = input("Did you complete all steps? (yes/no): ").strip().lower()

    if answer == "yes":
        # Check if folder exists
        if os.path.exists("data/mvtec"):
            print("\n✅ Dataset setup looks good!")
        else:
            print("\n⚠️ 'data/mvtec' folder not found. Please double-check your setup.")
    else:
        print("\n❌ Please complete the steps first before proceeding.")

    print("="*50)


if __name__ == "__main__":
    main()
import os
from src.modelTraining import trainModel
from src.prediction import filePrediction

def modelTrained(dataDirectory, pathToModel, pathToVectorizer):

    # is the model and vectorizer woorking?
    if os.path.exists(pathToModel) and os.path.exists(pathToVectorizer):
        print("Model and vectorizer are already trained and loaded.")
    else:
        # training in background
        print("Training the model in the background")
        trainModel(dataDirectory, pathToModel)
        print("Model training complete.")

def main():
    pathToModel = "models/model.pkl"
    pathToVectorizer = "models/vectorizer.pkl"

    modelTrained("data", pathToModel, pathToVectorizer)

    print("\nMalicious Browser Extension Detector!")
    while True:
        print("\nPlease choose an option:")
        print("1. Check if browser Extension is malicious")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            extensionPath = input("\nEnter the path to the file to scan: ")
            if not os.path.exists(extensionPath):
                print("Error: The file does not exist.")
                continue
            result = filePrediction(extensionPath, pathToModel, pathToVectorizer)
            print(f"\nThe file is classified as: {result}")
        elif choice == "2":
            print("\nExiting the application. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
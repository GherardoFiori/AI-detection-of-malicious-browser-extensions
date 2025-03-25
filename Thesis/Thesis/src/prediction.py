import os
import joblib

def filePrediction(extensionPath, pathToModel, pathToVectorizer):
    # Check if the model and vectorizer files exist
    if not os.path.exists(pathToModel) or not os.path.exists(pathToVectorizer):
        print("Error: Model or vectorizer not found. No training on model.")
        return

    # Load the model and vectorizer
    model = joblib.load(pathToModel)
    vectorizer = joblib.load(pathToVectorizer)

    # Read the file content
    with open(extensionPath, "r") as f:
        code = f.read()

    # Vectorize the code and make a prediction
    code_vec = vectorizer.transform([code])
    prediction = model.predict(code_vec)
    return "Malicious" if prediction[0] == 1 else "Benign"
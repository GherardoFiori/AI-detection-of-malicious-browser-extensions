import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from src.utils import load_data

def preprocessData(dataDirectory):
    # Load malicious and benign code for training
    maliciousExtensions= load_data(os.path.join(dataDirectory, "malicious"))  # Load malicious code
    beningExtensions = load_data(os.path.join(dataDirectory, "benign"))        # Load benign code

    # Label the data: 1 for malicious, 0 for benign
    maliciousLabels = [1] * len(maliciousExtensions)  # All malicious files are labeled as 1
    benignLabels = [0] * len(beningExtensions)       # All benign files are labeled as 0

    # Combine all the data collected in the one dataset
    files = maliciousExtensions + beningExtensions        
    labels = maliciousLabels + benignLabels     

    # converting to pandas
    df = pd.DataFrame({"code": files, "label": labels})

    # split training and testing
    X_train, X_test, y_train, y_test = train_test_split(df["code"], df["label"], test_size=0.2, random_state=42)

    # This process 
    vectorizer = TfidfVectorizer(max_features=1000)  
    X_train_vec = vectorizer.fit_transform(X_train)  
    X_test_vec = vectorizer.transform(X_test)       

    return X_train_vec, X_test_vec, y_train, y_test, vectorizer
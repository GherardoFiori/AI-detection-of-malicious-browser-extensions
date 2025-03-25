import os

def load_data(directory):
    data = []
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Read the content of each file and append it to the data list
        with open(os.path.join(directory, filename), "r") as f:
            data.append(f.read())
    return data
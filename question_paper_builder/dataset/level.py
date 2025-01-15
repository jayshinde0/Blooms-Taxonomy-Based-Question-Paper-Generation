import pickle

# Specify the absolute path to your PKL file
pkl_file_path = 'C:\\Users\Raj_2\\Desktop\\6th sem\\Mega project\\question_paper\\question_paper_builder\\dataset\\vectorizer.pkl'

# Open the PKL file in binary mode
with open(pkl_file_path, 'rb') as f:
    # Load the data from the PKL file
    data = pickle.load(f)

print(data)
# Now 'data' contains the Python object stored in the PKL file
# You can use 'data' as you would any other Python object

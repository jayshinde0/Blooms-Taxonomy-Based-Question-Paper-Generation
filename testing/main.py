import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
# Load the dataset
data = pd.read_csv("ML_QUESTION_Sheet1_final.csv")

# Preprocess the data
# data['question'] = data['question'].str.lower() # Convert text to lowercase
# data['question'] = data['question'].str.replace('[^\w\s]','') # Remove punctuation marks

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data['question'], data['marks'], test_size=0.2, random_state=42)

# Convert text data into numerical vectors
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Save the CountVectorizer model
with open('vectorizer.pkl', 'wb') as file:
    pickle.dump(vectorizer, file)

# Train the model
model = LinearRegression()
model.fit(X_train_vec, y_train)

# Evaluate the model
X_test_vec = vectorizer.transform(X_test)
y_pred = model.predict(X_test_vec)
mae = mean_absolute_error(y_test, y_pred)
print("Mean absolute error:", mae)

# Save the LinearRegression model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

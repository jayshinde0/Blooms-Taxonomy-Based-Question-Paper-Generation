import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
# Load the saved model
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
# Load the new questions from a CSV file
new_data = pd.read_csv('Machine_learning.csv')

# Preprocess the new questions
# new_data['question'] = new_data['question'].str.lower()
# new_data['question'] = new_data['question'].str.replace('[^\w\s]','')

# Transform the new questions into numerical vectors using the CountVectorizer that was fitted on the training data
X_new = vectorizer.transform(new_data['question'])

# Make predictions using the loaded model
y_new_pred = model.predict(X_new)
y_new_pred = np.array(y_new_pred)
y_new_pred = y_new_pred.astype(int)

new_data['predicted_marks'] = y_new_pred
print('*' * 50)
print(y_new_pred)
# Filter the new_data DataFrame based on predicted marks
new_data_4 = new_data[new_data['predicted_marks'] == 4]
new_data_5 = new_data[new_data['predicted_marks'] == 5]
new_data_6 = new_data[new_data['predicted_marks'] == 6]
new_data_7 = new_data[new_data['predicted_marks'] == 7]
new_data_8 = new_data[new_data['predicted_marks'] == 8]

# Select 2 questions for each of the marks using the head method
selected_data = pd.concat([new_data_4.sample(n=2, random_state=24), new_data_5.sample(n=2, random_state=24), new_data_6.sample(n=2, random_state=24), new_data_7.sample(n=2, random_state=24), new_data_8.sample(n=2, random_state=24)], axis=0)

print('*'*50)
print(selected_data)
selected_list = []
for _, row in selected_data[['question', 'predicted_marks']].iterrows():
    selected_dict = row.to_list()
    selected_list.append(selected_dict)

qus = []
[qus.extend([str(q), str(m)]) for q,m in selected_list]

print('*'*50)
print(qus)
# Add the predicted marks to the new_data DataFrame
# new_data['predicted_marks'] = selected_data
# print(new_data)
# Save the results to a CSV file

# # Save the selected data to a CSV file
# selected_data.to_csv('selected_data1.csv', index=False)
# new_data.to_csv('new_data_with_predictions.csv', index=False)

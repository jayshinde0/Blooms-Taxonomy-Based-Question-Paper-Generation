import pandas as pd

def predict_blooms_level(question):
    keywords = {
        "remenber": ["define", "list", "state", "label", "name", "recite", "recall", "write", "which", "what", "how", "duplicate", "memorize","repeat"],
        "understand": ["explain", "describe", "summarize", "contrast", "suggest","classify", "discuss","identify","locate","recognize","report","select","translate"],
        "apply": ["apply", "demonstrate", "use", "solve", "calculate", "show", "give", "example", "applications","execute","impliment","interpret","operate","schedule","sketch"],
        "analyze": ["analyze", "break down", "compare", "contrast", "differentiate", "distinguish", "discuss", "why", "find", "obtain","organize","relate","examine","experiment","question","test"],
        "evaluate": ["evaluate", "assess", "justify", "critique", "argue", "recommend", "prove", "draw", "elaborate", "specify","appraise","defend","judge","select","support","value","waigh"],
        "create": ["create", "design", "generate", "compose", "combine", "plan", "construct", "convert", "derive","assemble","conjecture","develope","formulate","author","investigate"],
    }

    predicted_levels = []

    for level, level_keywords in keywords.items():
        if any(keyword in question.lower() for keyword in level_keywords):
            predicted_levels.append(level)

    if predicted_levels:
        return predicted_levels
    else:
        return ["unknown"]

# Read the CSV file
df = pd.read_csv('ML_QUESTION_Sheet1_final.csv')

# Perform Bloom's level prediction for each question
df['blooms_level'] = df['question'].apply(predict_blooms_level)

# Save the updated dataframe to a new CSV file
df.to_csv('blooms_output.csv', index=False)

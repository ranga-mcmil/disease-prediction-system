import pandas as pd
import pickle
df = pd.read_csv('Training.csv')

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def symptoms_processor(symptoms):
    symptoms_df = df.drop(['prognosis', 'Unnamed: 133'],axis=1)
    symptoms_df = symptoms_df.loc[[0],:]
    symptoms_df.loc[0] = 0

    for symptom in symptoms:
        symptoms_df.loc[0,f"{symptom}"] = 1

    return symptoms_df

def get_prediction_results(symptoms_dataframe):
    result = model.predict(symptoms_dataframe)
    return (result[0],df['prognosis'].unique()[result[0]])

def predictions(symptoms):
    return get_prediction_results(symptoms_processor(symptoms))
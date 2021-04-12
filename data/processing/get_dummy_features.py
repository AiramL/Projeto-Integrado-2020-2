import pandas as pd
from pickle import dump

dataset = pd.read_csv('..\\dataset.csv')
symptom_list = pd.unique(dataset[['Symptom_1', 'Symptom_2', 'Symptom_3', 'Symptom_4',
       'Symptom_5', 'Symptom_6', 'Symptom_7', 'Symptom_8', 'Symptom_9',
       'Symptom_10', 'Symptom_11', 'Symptom_12', 'Symptom_13', 'Symptom_14',
       'Symptom_15', 'Symptom_16', 'Symptom_17']].values.ravel('K'))

dictionary = {ni: indi for indi, ni in enumerate(set(symptom_list))}

with open("dataset_dummy","wb") as data:
    dump(dictionary,data)



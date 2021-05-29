# Project Name: TEAPS - Triagem Eficiente e Ágil de Pacientes Sintomáticos 
#
# Authors:      Gustavo Camilo, Lucas Airam and Vicinicius Aguiar
# Affiliation:  Universidade Federal do Rio de Janeiro
#
#
#
#
# get_dummy_features.py reads the original dataset and assigns a number to every unique symptom, as classifiers accept numerical features only.

import pandas as pd
from pickle import dump

def get_data(dataset_path,write_path):
    dataset = pd.read_csv(dataset_path)
    symptom_list = pd.unique(dataset[['Symptom_1', 'Symptom_2', 'Symptom_3', 'Symptom_4',
           'Symptom_5', 'Symptom_6', 'Symptom_7', 'Symptom_8', 'Symptom_9',
           'Symptom_10', 'Symptom_11', 'Symptom_12', 'Symptom_13', 'Symptom_14',
           'Symptom_15', 'Symptom_16', 'Symptom_17']].values.ravel('K'))
    dictionary = {ni: indi for indi, ni in enumerate(set(symptom_list))}
    with open(write_path,"wb") as data:
        dump(dictionary,data)
    return dictionary
    

if __name__ == "__main__":
    d = get_data('..\\datasets\\original\\dataset.csv','..\\datasets\\transformed\\dataset_dummy')
    

# Project Name: TEAPS - Triagem Eficiente e Ágil de Pacientes Sintomáticos 
#
# Authors:      Gustavo Camilo, Lucas Airam and Vicinicius Aguiar
# Affiliation:  Universidade Federal do Rio de Janeiro
#
#
#
#
# get_dummy_features.py reads the original dataset and assigns a number to every unique disease,
# as scoring accept numerical class only.

import pandas as pd
from pickle import dump

def get_classes(dataset_path,write_path):
    dataset = pd.read_csv(dataset_path)
    symptom_list = pd.unique(dataset[['Disease']].values.ravel('K'))
    dictionary = {ni: indi for indi, ni in enumerate(set(symptom_list))}
    with open(write_path,"wb") as data:
        dump(dictionary,data)

if __name__ == "__main__":
    get_classes('..\\datasets\\original\\dataset.csv',"..\\datasets\\transformed\\class_dummy")

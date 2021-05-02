# Project Name: TEAPS - Triagem Eficiente e Ágil de Pacientes Sintomáticos 
#
# Authors:      Gustavo Camilo, Lucas Airam and Vicinicius Aguiar
# Affiliation:  Universidade Federal do Rio de Janeiro
#
#
#
#
#integrate_datasets.py integrates the covid dataset with the general diseases dataset

import pandas as pd
import numpy as np

COVID_DATASET_PATH = "..\\datasets\\transformed\\transformed_covid_dataset.csv"
DISEASE_DATASET_PATH = "..\\datasets\\original\\dataset.csv"
INTEGRATED_DATASET_PATH = "..\\datasets\\transformed\\integrated_dataset.csv"

#####################################################################
# Open datasets
#####################################################################

disease_dataset = pd.read_csv(DISEASE_DATASET_PATH)
covid_dataset = pd.read_csv(COVID_DATASET_PATH)

#####################################################################
# Adjust covid_dataset columns
#####################################################################

string_list = ['Disease']
for index in range(1,10):
    string_list.append('Symptom_'+str(index))

covid_dataset.columns = string_list
    

for index in range(8):
    sympton_string = 'Symptom_'+str(index+10)
    covid_dataset.insert(index+10,sympton_string,np.nan)

#####################################################################
# Add entries from covid_dataset to disease_dataset and save to file
#####################################################################

covid_sample = covid_dataset.sample(n=100)
disease_dataset = disease_dataset.append(covid_sample, ignore_index=True)

disease_dataset.to_csv(INTEGRATED_DATASET_PATH,index=False)




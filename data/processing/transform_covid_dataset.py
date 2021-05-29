# Project Name: TEAPS - Triagem Eficiente e Ágil de Pacientes Sintomáticos 
#
# Authors:      Gustavo Camilo, Lucas Airam and Vicinicius Aguiar
# Affiliation:  Universidade Federal do Rio de Janeiro
#
#
#
#
#transform_covid_dataset.py reads the original dataset and adapts it to the general diseases dataset

import pandas as pd
from pickle import dump


COVID_DATASET_PATH = "..\\datasets\\original\\Cleaned-Data.csv"

################################################
# Adapt covid dataset to symptom dataset
################################################

covid_dataset = pd.read_csv(COVID_DATASET_PATH)
covid_dataset = covid_dataset.loc[:, 'Fever':'Contact_Yes'].replace(1, pd.Series(covid_dataset.columns, covid_dataset.columns))
covid_dataset = covid_dataset.replace(0,'')

################################################
# Drop the columns that will not be used
################################################

covid_dataset = covid_dataset.drop(covid_dataset.loc[:,'None_Experiencing':'Contact_Yes'],axis=1)
covid_dataset = covid_dataset.drop(['None_Sympton'],axis=1)

################################################
# Modify symptons to comply with diseases dataset
################################################

covid_dataset = covid_dataset.replace('Difficulty-in-Breathing',' breathlessness')
covid_dataset = covid_dataset.replace('Fever',' high_fever')
covid_dataset = covid_dataset.replace('Tiredness',' fatigue')
covid_dataset = covid_dataset.replace('Dry-Cough',' cough')
covid_dataset = covid_dataset.replace('Sore-Throat',' throat_irritation')
covid_dataset = covid_dataset.replace('Pains',' chest_pain')
covid_dataset = covid_dataset.replace('Nasal-Congestion',' congestion')
covid_dataset = covid_dataset.replace('Runny-Nose',' runny_nose')
covid_dataset = covid_dataset.replace('Diarrhea',' diarrhoea')

################################################
# Insert column with disease name and save file
################################################
covid_dataset.insert(0,'Disease','Covid')
covid_dataset.to_csv('..\\datasets\\transformed\\transformed_covid_dataset.csv',index=False)




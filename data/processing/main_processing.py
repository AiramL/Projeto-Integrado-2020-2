# Project Name: TEAPS - Triagem Eficiente e Ágil de Pacientes Sintomáticos 
#
# Authors:      Gustavo Camilo, Lucas Airam and Vicinicius Aguiar
# Affiliation:  Universidade Federal do Rio de Janeiro
#
#
#
#
# main_processing.py process all datasets


from get_dummy_class import get_classes
from get_dummy_dataset import save_transformation
from get_dummy_dataset import translate_features
from get_dummy_features import get_data




get_classes('..\\datasets\\transformed\\integrated_dataset.csv',"..\\datasets\\transformed\\class_dummy")
get_data('..\\datasets\\transformed\\integrated_dataset.csv','..\\datasets\\transformed\\dataset_dummy')
save_transformation("..\\datasets\\transformed\\dataset_transformed",translate_features("..\\datasets\\transformed\\dataset_dummy",'..\\datasets\\transformed\\integrated_dataset.csv'))




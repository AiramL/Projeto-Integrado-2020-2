# Project Name: TEAPS - Triagem Eficiente e Ágil de Pacientes Sintomáticos 
#
# Authors:      Gustavo Camilo, Lucas Airam and Vicinicius Aguiar
# Affiliation:  Universidade Federal do Rio de Janeiro
#
#
#
#
# get_dummy_dataset.py changes the features in the original dataset to numerical features

from pickle import load
from pickle import dump

def translate_label_file(dictionary_path,label_vector):
    with open(dictionary_path,'rb') as dataset_dictionary:
        dictionary = load(dataset_dictionary)
        tmp = []
        for element in label_vector:
            if element not in dictionary.keys():
                return "invalid label"
            else:
                tmp.append(dictionary[element])
    return tmp

def translate_label(dictionary,label_vector):
    tmp = []
    for element in label_vector:
        if element not in dictionary.keys():
            if element != "":
                tmp.append(element)
            else:
                tmp.append(0)
        else:
            tmp.append(dictionary[element])
    return tmp


def translate_features(dictionary_path,dataset_path):
    dummy_file = open(dictionary_path,"rb")
    dictionary = load(dummy_file)
    with open(dataset_path,'r') as dataset:
        translation = []
        first_line = True
        for line in dataset:
            if first_line:
                pass
            else:
                line_split = line[:-1].split(',')
                translation.append(translate_label(dictionary,line_split))
            first_line = False
    return translation


def save_transformation(write_path,transformation):
    with open(write_path,"wb") as save:
        dump(transformation,save)
    
    
if __name__ == "__main__":
    save_transformation("..\\datasets\\transformed\\dataset_transformed",translate_features("..\\datasets\\transformed\\dataset_dummy",'..\\datasets\\original\\dataset.csv'))

# Project Name: TEAPS - Triagem Eficiente e Ágil de Pacientes Sintomáticos 
#
# Authors:      Gustavo Camilo, Lucas Airam and Vicinicius Aguiar
# Affiliation:  Universidade Federal do Rio de Janeiro
#
#
#
#
# create_model.py: fit a model with a dataset  


from sklearn import tree
from random import randint
from pickle import load
from pickle import dump
import pickle

def creat_tree_model(dataset_path,write_path):
    dataset = load(open(dataset_path,"rb"))
    size = 0.7
    sample_size = len(dataset)*size 

     
    X_training = []
    Y_training = []
    X_test = []
    Y_test = []

    while(len(dataset) > sample_size):
        seed = randint(0,len(dataset)-1)
        data = dataset.pop(seed)
        X_test.append(data[1:])
        Y_test.append(data[0])


    for data in dataset:
        X_training.append(data[1:]) 
        Y_training.append(data[0])

        
    classifier = tree.DecisionTreeClassifier(max_depth=23)
    classifier = classifier.fit(X_training,Y_training)

    with open(write_path,"wb") as writer:
        dump(classifier,writer)

    with open(write_path+"_test_data","wb") as writer:
        dump([X_test,Y_test],writer)

    
        
    


if __name__ == "__main__":
    creat_tree_model('..\\..\\data\\datasets\\transformed\\dataset_transformed','..\\model')
    


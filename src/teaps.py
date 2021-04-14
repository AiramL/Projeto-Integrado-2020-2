from sklearn import tree
from random import randint
from sklearn.metrics import average_precision_score
import pickle 
from sklearn.metrics import label_ranking_average_precision_score

# load dataset
f = open('..\\data\\datasets\\dataset_transformed',"rb")
dataset = pickle.load(f)
size = 0.7
sample_size = len(dataset)*size  # percentage of traning sample size

 
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




    
classificador = tree.DecisionTreeClassifier(max_depth=23)
classificador = classificador.fit(X_training,Y_training)


result = classificador.predict(X_test)
label_ranking_average_precision_score(Y_test, result)







##if __name__ == "__main__":
##    #dicionario = {}
##    lista = []
##
##    
##    counter = 0;
##    for line in f:
##        if counter == 0:
##            pass
##        else:
##            line_split = line.split(',')
##            for item in line_split[1:]:
##                if item not in lista:
##                    lista.append(item)
##        counter = 1
##    print(lista)
##    print(len(lista))
            

    
    


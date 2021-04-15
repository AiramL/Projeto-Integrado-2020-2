# Project Name: TEAPS - Triagem Eficiente e Ágil de Pacientes Sintomáticos 
#
# Authors:      Gustavo Camilo, Lucas Airam and Vicinicius Aguiar
# Affiliation:  Universidade Federal do Rio de Janeiro
#
#
#
#
# model_classification.py: results of a model classification



from pickle import load
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix

                
def visualize_confusion_matriz(model,model_test_data):
    dataset = load(open(model_test_data,"rb"))
    classifier = load(open(model,"rb"))
    X_test = dataset[0]
    Y_test = dataset[1]
    plot_confusion_matrix(classifier, X_test, Y_test)
    plt.show()
    


if __name__ == "__main__":
    visualize_confusion_matriz("..\\..\\model\\classifier","..\\..\\model\\model_test_data")    









# Project Name: TEAPS - Triagem Eficiente e Ágil de Pacientes Sintomáticos 
#
# Authors:      Gustavo Camilo, Lucas Airam and Vicinicius Aguiar
# Affiliation:  Universidade Federal do Rio de Janeiro
#
#
#
#
# model_structure.py: structure of a model 



from pickle import load
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


                
def visualize_model_structure(model_path):
    classifier = load(open(model_path,"rb"))
    plt.figure()
    plot_tree(classifier)
    plt.show()


if __name__ == "__main__":
    visualize_model_structure("..\\..\\model\\classifier")









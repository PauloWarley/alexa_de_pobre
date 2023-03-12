#Importa os datasets que vem com o scikit learn
from sklearn import datasets
#Guarda na variável iris o dataset iris
iris = datasets.load_iris()
#Armazena a matriz de recurso (feature) em "x"
features = iris.data[: , [0,1,2,3]]
#Armazena o vetor de resposta em "y"
targets = iris.target
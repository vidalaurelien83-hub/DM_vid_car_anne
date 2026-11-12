from sklearn.datasets import fetch_openml

directory = "data"
#telecharger jeu de donnée MNIST
mnist = fetch_openml('mnist_784', version=1, data_home=directory, as_frame=False, parser='liac-arff')


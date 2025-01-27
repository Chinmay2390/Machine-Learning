# import scipy
# print(scipy.__version__)

# loading iris dataset
from sklearn.datasets import load_iris
iris = load_iris()

x = iris.data   
y = iris.target

feature_names1 = iris.feature_names
target_names1 = iris.target_names

print(feature_names1)
print("---------------------------------------")
print(target_names1)

print("TYPE OF X",type(x))
print("---------------------------------------")
print("FIRST 5 ROWS:")
print(x[:5])
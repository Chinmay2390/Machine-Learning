import pandas as pd

# import os
# print(os.getcwd())

# df = pd.read_csv("weather.csv")

# getting size and columns
# print(df.shape)
# print(df.columns)

# getting the feature matrix(X) and response vector(y)
# X = df[df.columns[:-1]]
# y = df[df.columns[-1]]

# print(X.head())
# print("---------------------------------------")
# print(y.head())


# now its time to to load the iris dataset and do splitting on it
from sklearn.datasets import load_iris
iris = load_iris()

X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.4,random_state=1)

# print(X_train.shape)
# print(y_train.shape)

# print(X_test.shape)
# print(y_test.shape)

# importing the necessory model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)

# training the model on the X_train and y_train
knn.fit(X_train,y_train)

# predicting and storing in y_pred
y_pred = knn.predict(X_test)

# comparing the performance of model
from sklearn import metrics
print("knn model accuracy:",metrics.accuracy_score(y_test,y_pred))

# giving out-of-sample input and checking the output
input = [[3,5,4,2],[2,3,5,4]]
pred = knn.predict(input)

pred_species = [iris.target_names[p] for p in pred]
print("PREDICTION ON SAMPLE INPUT:",pred_species)


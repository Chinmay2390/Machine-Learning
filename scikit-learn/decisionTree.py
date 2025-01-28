import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer

X,y = load_breast_cancer(return_X_y=True)
X_df = pd.DataFrame(X, columns=load_breast_cancer().feature_names)
y_df = pd.Series(y, name="Target")

print(X_df.head())
print("***********************")
print(y_df.head())

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

print("1:",X_train.shape)
print("2:",y_train.shape)

print("3:",X_test.shape)
print("4:",y_test.shape)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train,y_train)

predictions = clf.predict(X_test)
print('ACCURACY:',accuracy_score(y_test,predictions))

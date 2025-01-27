from sklearn.datasets import load_digits
df = load_digits()

# print(dir(df))

# print(df.images[0])

# import matplotlib.pyplot as plt

# def plot_multi(i):
#     nplots = 16
#     fig = plt.figure(figsize=(15,15))
#     for j in range(nplots):
#         plt.subplot(4,4,j+1)
#         plt.imshow(df.images[i+j],cmap="binary")
#         plt.title(df.target[i+j])
#         plt.axis('off')

#     plt.show()

# plot_multi(0)

# flattning the images from 2d 8*8 array to single array of 64 values
y = df.target
x = df.images.reshape((len(df.images),-1))

# print(x.shape)
# print(x[0])

# splitting data for training and testing
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.4)

# print(X_train.shape)
# print(y_train.shape)
print("*******************************************")
# print(X_test.shape)
# print(y_test.shape)

from sklearn.neural_network import MLPClassifier

# calling the MLP classifier with specific parameters
mlp = MLPClassifier(hidden_layer_sizes=(15,),
                    activation='logistic',
                    alpha=1e-4, solver='sgd',
                    tol=1e-4, random_state=1,
                    learning_rate_init=.1,
                    verbose=True)

mlp.fit(X_train,y_train)

predictions = mlp.predict(X_test)
print(predictions[:50])
print('***********************************')
print(y_test[:50])

from sklearn.metrics import accuracy_score
print("ACCURACY FOR DIGIT RECOGNITION:",accuracy_score(y_test,predictions))



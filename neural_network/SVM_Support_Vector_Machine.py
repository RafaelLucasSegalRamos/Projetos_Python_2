from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC


x, y = load_iris(return_X_y=True, as_frame=True)

X = x.loc[y.isin([0, 1]), ['petal length (cm)', 'petal width (cm)']]
Y = y.loc[y.isin([0, 1])]

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.5)

# fig, ax = plt.subplots()
#
# ax.scatter(x_train['petal length (cm)'], x_train['petal width (cm)'], c=y_train, s=75)
#
# plt.show()

clf = SVC().fit(x_train, y_train)

y_pred = clf.predict(x_test)

fig, ax = plt.subplots()

ax.scatter(x_test['petal length (cm)'], x_test['petal width (cm)'], c=y_pred, s=75)

fig, ax = plt.subplots()

ax.scatter(x_test['petal length (cm)'], x_test['petal width (cm)'], c=y_test, s=75)

plt.show()

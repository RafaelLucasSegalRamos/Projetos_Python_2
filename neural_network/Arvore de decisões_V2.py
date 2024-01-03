from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np

bd = load_iris()
iris = pd.DataFrame(bd['data'], columns=[bd.feature_names])
iris.columns = bd.feature_names
iris['target'] = bd.target
print("Pre-edit:", iris.target.value_counts())
iris1 = iris.loc[iris.target.isin([1, 2]), ['petal length (cm)', 'petal width (cm)',
                                            'target']]  # tambem houve teste subtituindo [0, 1] por [1, 2]
print("Pos-edit:", iris1.target.value_counts())
X = iris.drop("target", axis=1)
Y = iris["target"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

clf = tree.DecisionTreeClassifier(random_state=42).fit(X_train, Y_train)
fig, ax = plt.subplots(figsize=(10, 8))
print(f"Score: {clf.score(X_train, Y_train) * 100}%")
tree.plot_tree(clf, ax=ax, feature_names=X_train.columns)

fig, ax = plt.subplots()
ax.scatter(X_test['petal length (cm)'], X_test['petal width (cm)'], c=Y_test)

# plt.show()

y_pred = clf.predict(X_test)

print(f"Score: {confusion_matrix(Y_test, y_pred)}%")

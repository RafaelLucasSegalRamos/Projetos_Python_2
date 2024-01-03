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
X = iris1.drop("target", axis=1)
Y = iris1["target"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

fig, ax = plt.subplots()
# gráfico do treino
ax.scatter(X_train['petal length (cm)'], X_train['petal width (cm)'], c=Y_train)

ax.set_xlabel('petal length (cm)')
ax.set_ylabel('petal width (cm)')
ax.set(xlim=(2.8, 7), xticks=[3, 4, 5, 6, 7],
       ylim=(0.9, 2.7), yticks=[0.5, 1, 1.5, 2, 2.5, 3])

# ax.plot([1, 5], [0.8, 0.8], c='red')
ax.plot([5.05, 5.05], [0.4, 2.89], c='red')
ax.plot([2.9, 5.05], [1.9, 1.9], c='red')
ax.plot([2.9, 5.05], [1.65, 1.65], c='red')
ax.plot([4.65, 4.65], [1.65, 1.9], c='red')

modelo = tree.DecisionTreeClassifier(random_state=42)
modelo = modelo.fit(X_train, Y_train)
print("\nAfter fit:")
print("Score:", modelo.score(X_train, Y_train))
# gráfico dos pensamentos que a IA teve
fig, ax = plt.subplots()

tree.plot_tree(modelo, ax=ax, feature_names=X_train.columns)

y_pred = modelo.predict(X_test)
print("\nAfter predict:")

matrix = confusion_matrix(Y_test, y_pred)
print(matrix)

# Gráfico do teste feito com outras variaveis
fig, ax = plt.subplots()
ax.scatter(X_test['petal length (cm)'], X_test['petal width (cm)'], c=Y_test)

ax.set_xlabel('petal length (cm)')
ax.set_ylabel('petal width (cm)')

ax.plot([5.05, 5.05], [0.4, 2.89], c='red')
ax.plot([2.9, 5.05], [1.9, 1.9], c='red')
ax.plot([2.9, 5.05], [1.65, 1.65], c='red')
ax.plot([4.65, 4.65], [1.65, 1.9], c='red')

plt.show()

# Link do video:  https://www.youtube.com/watch?v=aNrdgC0lIZ8

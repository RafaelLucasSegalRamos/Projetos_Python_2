from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

dados = pd.DataFrame({
    'A': [1, 1.5, 2, 1.5, -1, -0.5, 0, -0.5],
    'A2': [-0.5, 0, -0.5, -1, 1.5, 2, 1.5, 1],
    'B': [1, 1.5, 1, 0.5, -1, -0.5, -1, -1.5],
    'B2': [-1.5, -1, -0.5, -1, 0.5, 1, 1.5, 1],
    'y': [1, 1, 1, 1, 0, 0, 0, 0],
    'y2': [0, 0, 0, 0, 1, 1, 1, 1]
})

dados_pred = pd.DataFrame({
    'A': [2.5, 1.8, 0.5, -1, -1],
    'A2': [2.5, 1.8, 0.5, -1, -1],
    'B': [2, 1, 0, 0, -1.5],
    'B2': [2, 1, 0, 0, -1.5],
})



# ax.scatter(dados.A, dados.B, c=dados.y, cmap='viridis')
# ax.scatter(dados_pred.A, dados_pred.B, c='red', marker='s')
# plt.show()

vizinhos = KNeighborsClassifier(n_neighbors=3)
x = dados[['A', 'B']]
y = dados.y
vizinhos = vizinhos.fit(x, y)

X_teste = dados_pred[['A', 'B']]

y_pred = vizinhos.predict(X_teste)
# ax.scatter(dados.A, dados.B, c=dados.y, cmap='viridis')
# ax.scatter(dados_pred.A, dados_pred.B, c=y_pred, marker='s')
# plt.show()

iris = load_iris()
iris_bd = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_bd['target'] = iris.target
iris1 = iris_bd.loc[iris_bd.target.isin([1, 2]), ['petal length (cm)', 'petal width (cm)', 'target']]
X = iris1.drop('target', axis=1)
y = iris1['target']

x_treino, x_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=42)

# fig, ax = plt.subplots()
#
# ax.scatter(x_treino['petal width (cm)'], x_treino['petal length (cm)'], c=y_treino, cmap='viridis')
#
# ax.set(xlim=(0.9, 2.6), xticks=[1, 1.5, 2, 2.5], ylim=(3, 7), yticks=[3, 4, 5, 6, 7])


vizinhos = KNeighborsClassifier(n_neighbors=3)
vizinhos = vizinhos.fit(x_treino, y_treino)
y_pred = vizinhos.predict(x_teste)

print(f"Score: {accuracy_score(y_teste, y_pred) * 100:.2f}%")
print(f"Score: {confusion_matrix(y_teste, y_pred)}%")


# fig, ax = plt.subplots()
#
# ax.scatter(x_teste['petal width (cm)'], x_teste['petal length (cm)'], c=y_teste, cmap='RdYlGn')
#
# ax.set(xlim=(0.9, 2.6), xticks=[1, 1.5, 2, 2.5], ylim=(3, 7), yticks=[3, 4, 5, 6, 7])
#

fig, ax = plt.subplots()


ax.scatter(x_teste['petal width (cm)'], x_teste['petal length (cm)'], c=y_teste, cmap='viridis')
ax.scatter(x_teste['petal width (cm)'], x_teste['petal length (cm)'], c=y_pred, cmap='RdYlGn', alpha=0.2)
ax.set(xlim=(0.9, 2.6), xticks=[1, 1.5, 2, 2.5], ylim=(3, 7), yticks=[3, 4, 5, 6, 7])

plt.show()
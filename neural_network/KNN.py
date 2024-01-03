from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import matplotlib.pyplot as plt

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

fig, ax = plt.subplots()

# ax.scatter(dados.A, dados.B, c=dados.y, cmap='viridis')
# ax.scatter(dados_pred.A, dados_pred.B, c='red', marker='s')
# plt.show()

vizinhos = KNeighborsClassifier(n_neighbors=3)
x = dados[['A', 'B']]
y = dados.y
vizinhos = vizinhos.fit(x, y)

X_teste = dados_pred[['A', 'B']]

y_pred = vizinhos.predict(X_teste)
print(y_pred)
ax.scatter(dados.A, dados.B, c=dados.y, cmap='viridis')
ax.scatter(dados_pred.A, dados_pred.B, c='red', marker='s')
plt.show()


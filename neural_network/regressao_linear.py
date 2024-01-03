import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

dados = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [1.3, 1.8, 3.5, 4, 4.6]
})

dados.x.values.reshape(-1, 1)
dados.y.values.reshape(-1, 1)
n_x = dados.x.values.reshape(-1, 1)

reg = LinearRegression().fit(n_x, dados.y)
a = reg.coef_[0]
b = reg.intercept_

fig, ax = plt.subplots()
dados['y_reta'] = dados.x

ax.scatter(dados.x, dados.y)
ax.scatter(dados.x, dados.y_reta)
ax.plot(dados.x, dados.y_reta, "--r", c='darkgreen') # reta que eu criei (a verde)

x = dados.x.values
y = a * x + b
ax.plot(x, y, c="red") # reta que o sklearn criou (a vermelha)
plt.show()

dados['y_pred'] = reg.predict(dados.x.values.reshape(-1, 1))
print(dados['y_pred'])
print("\nProvando que a reta do sklearn é superior: (Pois a regrssão linear é a reta que minimiza o erro ao quadrado)")
dados["erro_reta"] = mean_squared_error(dados.y, dados.y_reta)
print(f"Erro da reta que eu criei: {sum(dados["erro_reta"]):2f}")
dados["erro_pred"] = mean_squared_error(dados.y, dados.y_pred)
print(f"Erro da reta do sklearn: {sum(dados["erro_pred"]):2f}")

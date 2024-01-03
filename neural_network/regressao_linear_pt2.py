import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
# agora mexendo com o bd do sklearn

bd = fetch_california_housing()
casas = pd.DataFrame(bd.data, columns=bd.feature_names)
casas.columns = bd.feature_names

casas['MedHouseVal'] = bd.target

x = casas.drop('MedHouseVal', axis=1)
y = casas['MedHouseVal']

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.33, random_state=42)

reg = LinearRegression().fit(x_treino, y_treino)

y_pred = reg.predict(x_teste)
erro_pred = mean_squared_error(y_teste, y_pred)
print(f"Erro da reta do sklearn: {erro_pred:2f}")

fig, ax = plt.subplots()

ax.scatter(y_pred, y_teste)
ax.plot([1,5], [1,5], "--r", c='red')

plt.show()
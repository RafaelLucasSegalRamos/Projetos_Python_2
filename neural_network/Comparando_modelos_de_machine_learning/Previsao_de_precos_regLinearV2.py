import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# from pandas_profiling import ProfileReport

pd.options.display.float_format = '{:,.2f}'.format

# Importando os dados
base = pd.read_csv('melb_data.csv')
base = base.drop(['Suburb', 'Address', 'SellerG', 'Date', 'BuildingArea', "YearBuilt"], axis=1)
# Retirando colunas que possuem informações especificas demais e que possuam muitos zeros.

base2 = base[['Rooms', 'Price', 'Bathroom', 'Bedroom2', 'Car', 'Landsize', "Longtitude", "Lattitude", "Distance", "Postcode", "Propertycount"]]
base2 = base2.dropna(axis=0)

Y = base2['Price']
X = base2.drop('Price', axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

modelo_reg2 = LinearRegression()
reg = modelo_reg2.fit(X_train, Y_train)

y_regressao = reg.predict(X_test)

plt.figure(figsize=(10, 10))
sns.scatterplot(x=Y_test.values / 1000000, y=y_regressao / 1000000)
plt.ylim(0, 10)
plt.xlim(0, 10)
plt.show()

print(f"Erro quadratico da regressão linear: {mean_squared_error(Y_test, y_regressao):.2f}")
print(f"R2 da regressão linear: {r2_score(Y_test, y_regressao)*100:.2f}%")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# from pandas_profiling import ProfileReport

pd.options.display.float_format = '{:,.2f}'.format

# Importando os dados
base = pd.read_csv('melb_data.csv')
base = base.drop(['Suburb', 'Address', 'SellerG', 'Date', 'BuildingArea', "YearBuilt"], axis=1)
# Retirando colunas que possuem informações especificas demais e que possuam muitos zeros.

# plt.figure(figsize=(13, 8))
# sns.heatmap(base.corr(), annot=True, cmap='YlGnBu')
# plt.show()

base1 = base[['Rooms', 'Price', 'Bathroom', 'Bathroom2', 'Car', 'Landsize']]

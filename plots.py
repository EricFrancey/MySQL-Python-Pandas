import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/products.csv')

# df.plot(kind = 'scatter', x = 'productID', y = 'unitsInStock')

df["unitsInStock"].plot(kind = 'hist')
plt.show()
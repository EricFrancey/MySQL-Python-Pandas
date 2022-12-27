import pandas as pd
import matplotlib.pyplot as plt

def productsHist():
    df = pd.read_csv('data/products.csv')
    df["unitsInStock"].plot(kind = 'hist')
    plt.show()
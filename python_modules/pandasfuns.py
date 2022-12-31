import pandas as pd

data = pd.read_csv('data/products.csv')
df = pd.DataFrame(data)

def cov():
    print("Covariance")
    print(df.cov(numeric_only = True))

def sum():
    print("sum============")
    print(df.sum(numeric_only = True))

def description():
    print("describe============")
    print(df.describe())

#query
#drop
#loc
#truncate



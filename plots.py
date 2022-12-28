import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def plotHist(table, graphtype, field1, field2):
    data = pd.read_csv(f'data/{table}.csv')
    data.plot(kind = graphtype, x = field1, y = field2, title = table)
    plt.savefig(f"savedplots/{table}-{field2} " + datetime.now().strftime("%d-%m-%Y %H_%M_%S") + ".jpg")
    plt.close()
    print("==================")
    print("jpg created.")
    print("==================")

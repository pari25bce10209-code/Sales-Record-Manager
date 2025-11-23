# pandas_helper.py
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
def showChart():
    df = pd.read_csv("sales.csv")
    totals = df.groupby("Date")["Total"].sum()
    totals.plot(kind="bar")
    plt.title("Sales by Date")
    plt.xlabel("Date")
    plt.ylabel("Total")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
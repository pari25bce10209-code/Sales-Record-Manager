# pandas_helper.py
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
def showChart():
    df = pd.read_csv("sales.csv")
    totals = df.groupby("Date")["Total"].sum()
    # Group sales by 'Date' and calculate the sum of 'Total' for each date
    totals.plot(kind="bar")
    plt.title("Sales by Date")  # Add chart title and axis labels
    plt.xlabel("Date")
    plt.ylabel("Total") 
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout() # Adjust layout so labels and titles fit nicely
    plt.show()  # Display the chart in a window

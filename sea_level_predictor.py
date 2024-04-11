import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    feature = "Year"
    response = "CSIRO Adjusted Sea Level"

    x = df[feature]
    y = df[response]

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x, y)
    
    # Create first line of best fit
    res = linregress(x, y)
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = res.slope * x_pred + res.intercept
    ax.plot(x_pred, y_pred, "r")

    # Create second line of best fit
    mm_df = df.loc[df["Year"] >= 2000]
    mm_x = mm_df[feature]
    mm_y = mm_df[response]
    mm_res = linregress(mm_x, mm_y)
    mm_x_pred = pd.Series([i for i in range(2000, 2051)])
    mm_y_pred = mm_res.slope * mm_x_pred + mm_res.intercept
    ax.plot(mm_x_pred, mm_y_pred, "g")

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
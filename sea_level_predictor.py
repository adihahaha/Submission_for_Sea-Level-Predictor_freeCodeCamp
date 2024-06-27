import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    data = r'epa-sea-level.csv'
    df = pd.read_csv(data)

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(11, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Create first line of best fit
    years = np.arange(df['Year'].min(), 2051)
    plt.plot(
        years,
        linregress(df['Year'], df['CSIRO Adjusted Sea Level']).intercept +
        linregress(df['Year'], df['CSIRO Adjusted Sea Level']).slope * years)
    # Create second line of best fit
    new_df = df[df["Year"] >= 2000].copy().reset_index(drop=True)
    new_years = np.arange(new_df['Year'].min(), 2051)
    plt.plot(
        new_years,
        linregress(new_df['Year'],
                   new_df['CSIRO Adjusted Sea Level']).intercept +
        linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level']).slope *
        new_years)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend(['Original Data', 'Original Prediction', 'New Prediction'])

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data", alpha=0.7)


    # Create first line of best fit
    slope_all, intercept_all, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = range(1880, 2051)  # Predict up to 2050
    sea_levels_extended = [intercept_all + slope_all * year for year in years_extended]
    plt.plot(years_extended, sea_levels_extended, 'r', label="Best Fit (1880-2050)")

    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]  # Filter data from 2000 onwards
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = range(2000, 2051)  # Predict up to 2050
    sea_levels_recent = [intercept_recent + slope_recent * year for year in years_recent]
    plt.plot(years_recent, sea_levels_recent, 'g', label="Best Fit (2000-2050)")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
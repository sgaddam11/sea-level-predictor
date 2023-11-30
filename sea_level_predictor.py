import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue',marker='|')

    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    future_years = range(1880, 2051)
  
    plt.plot(future_years, slope * future_years + intercept, linestyle='dashed', label='Extended Line to 2050')

    # Create second line of best fit
    recent_data = df[df['Year'] >= 2000]
  
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
  
  
    future_years = range(2000, 2051)
    plt.plot(future_years, slope_recent * future_years + intercept_recent, linestyle='dashed', color='red', label='Extended Line to 2050')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from vega_datasets import data

# Load the stock dataset
df = data.stocks()

def explore_data(df):
    """Function to explore the stock dataset."""
    print("Dataset Overview:")
    print(df.info())
    print("\nFirst 5 rows of the dataset:")
    print(df.head())
    
    # Visualize the stock prices over time
    plt.figure(figsize=(13, 7))
    sns.lineplot(data=df, x='date', y='price', hue='symbol')
    plt.title('Stock Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(title='Stock Symbol')
    plt.show()

if __name__ == "__main__":
    explore_data(df)
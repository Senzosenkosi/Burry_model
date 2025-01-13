import pandas as pd

def load_data(file_path):
    """Load stock data from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean the stock data by handling missing values and duplicates."""
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def transform_features(df):
    """Transform features for analysis, such as converting dates."""
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    return df

def preprocess_data(file_path):
    """Main function to preprocess stock data."""
    df = load_data(file_path)
    df = clean_data(df)
    df = transform_features(df)
    return df
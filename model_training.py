import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_model(df):
    # Preprocess the data
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df['Return'] = df['Close'].pct_change()
    df.dropna(inplace=True)

    # Features and target variable
    X = df[['Open', 'High', 'Low', 'Volume']]
    y = df['Return']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')

    return model

if __name__ == "__main__":
    # Example usage
    df = pd.read_csv('path_to_your_stocks_data.csv')  # Update with the actual path to your dataset
    trained_model = train_model(df)
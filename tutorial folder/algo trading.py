import time
import datetime
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_and_display_data(ticker, start_time, end_time):
    # Fetch the latest data
    data = yf.download(ticker, period="1d", interval="1m")

    # Filter data based on start and end times
    data = data.loc[start_time:end_time]

    # Calculate the technical indicators
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['EMA_50'] = data['Close'].ewm(span=50, adjust=False).mean()
    data['RSI_14'] = data['Close'].diff().where(lambda x: x > 0, 0).rolling(window=14).mean() / (-data['Close'].diff().where(lambda x: x < 0, 0).rolling(window=14).mean())
    data['RSI_14'] = 100 - (100 / (1 + data['RSI_14']))

    # Plot the results
    plt.figure(figsize=(14, 8))

    # Plot closing price and Moving Averages
    plt.subplot(2, 1, 1)  # First subplot
    plt.plot(data['Close'], label='Close Price', color='black')
    plt.plot(data['SMA_50'], label='50-day SMA', color='blue', linestyle='--')
    plt.plot(data['EMA_50'], label='50-day EMA', color='red', linestyle='--')
    plt.title(f"{ticker} Stock Price and Moving Averages")
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()

    # Plot RSI
    plt.subplot(2, 1, 2)  # Second subplot
    plt.plot(data['RSI_14'], label='RSI (14)', color='green')
    plt.axhline(70, linestyle='--', alpha=0.5, color='red')
    plt.axhline(30, linestyle='--', alpha=0.5, color='blue')
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel('Time')
    plt.ylabel('RSI')
    plt.legend()

    # Adjust x-axis limits to zoom in
    plt.xlim(data.index[0], data.index[-1])

    plt.tight_layout()
    plt.show()

    # Update the plot every second
    while True:
        # Fetch the latest data
        new_data = yf.download(ticker, period="1d", interval="1m", start=data.index[-1] + pd.Timedelta(minutes=1))

        # Append new data
        data = pd.concat([data, new_data])

        # Update the plot
        plt.cla()  # Clear the plot
        plt.plot(data['Close'], label='Close Price', color='black')
        plt.plot(data['SMA_50'], label='50-day SMA', color='blue', linestyle='--')
        plt.plot(data['EMA_50'], label='50-day EMA', color='red', linestyle='--')
        plt.title(f"{ticker} Stock Price and Moving Averages")
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.legend()

        plt.subplot(2, 1, 2)  # Second subplot
        plt.plot(data['RSI_14'], label='RSI (14)', color='green')
        plt.axhline(70, linestyle='--', alpha=0.5, color='red')
        plt.axhline(30, linestyle='--', alpha=0.5, color='blue')
        plt.title('Relative Strength Index (RSI)')
        plt.xlabel('Time')
        plt.ylabel('RSI')
        plt.legend()

        # Adjust x-axis limits to zoom in
        plt.xlim(data.index[0], data.index[-1])

        plt.draw()  # Update the plot
        time.sleep(1)  # Update every second

if __name__ == "__main__":
    ticker = "AAPL"  # Replace with your desired ticker
    while True:
        # Specify start and end times for the desired month and day
        start_time = "2023-10-01 09:00:00"  # Replace with your desired start time
        end_time = datetime.datetime.now().strftime("%Y-%m-%d 16:30:00")  # Replace with your desired end time

        fetch_and_display_data(ticker, start_time, end_time)
        time.sleep(1)  # Update every second
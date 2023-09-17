# INF601 - Advanced Programming with Python
# Brayan Gomez
# Mini project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


def get_closing(ticker_list:list):
    # get 10 day history of each stock
    hist = [yf.Ticker(stock).history(period="10d") for stock in ticker_list]

    closing_list = {}
    for i, stock in enumerate(hist):
        # closing for 10 days
        data = [f"{closing:.2f}" for closing in stock["Close"]]
        closing_list[ticker_list[i]] = data  # add entry

    return closing_list


def get_closing_one(ticker):
    # Get 10 day history of a stock
    hist = yf.Ticker(ticker).history(period="10d")
    # Get the closing price for each day
    closing_list = [price for price in hist["Close"]]

    return closing_list


stocks = ["META", "AMZN", "GOOG", "NFLX", "MSFT"]
for stock in stocks:
    # y-axis for our graph
    stock_closing = np.array(get_closing_one(stock))
    # x-axis for our graph
    days = list(range(1, len(stock_closing) + 1))
    # Plot the graph
    plt.plot(days, stock_closing)

    # get the min, max of our y-axis
    prices = stock_closing
    prices.sort()
    low_price = prices[0]
    high_price = prices[-1]
    # set the x-axis & y-axis
    plt.axis([1, 10, low_price - 1, high_price + 1])

    # Labels for the graph
    plt.title(f"Closing Price for {stock}")
    plt.xlabel("Days")
    plt.ylabel("Closing Price")
    # render graph
    plt.show()
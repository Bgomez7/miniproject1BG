# INF601 - Advanced Programming with Python
# Brayan Gomez
# Mini project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def get_stocks():
    stocks = []
    # get 5 stocks
    for i in range(1,6):
        # verify the stocks
        while True:
            print(f"Enter stock ticker {i}")
            ticker = input(">")
            try:
                print("Verifying...")
                yf.Ticker(ticker).info
                print("Valid")
                stocks.append(ticker)
                break
            except:
                print("Invalid stock ticker")
    return stocks



def get_closing(ticker):
    # Get 10 day history of a stock
    hist = yf.Ticker(ticker).history(period="10d")
    # return the closing price for each day
    return [price for price in hist["Close"]]


def graph_stock(stock):
    # y-axis for our graph
    stock_closing = np.array(get_closing(stock))
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

    # Save files to charts directory
    save_file = f"charts/{stock}.png"
    plt.savefig(save_file)

    # render graph
    plt.show()


# Create charts directory
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

for stock in get_stocks():
    get_closing(stock)
    graph_stock(stock)

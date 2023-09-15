# INF601 - Advanced Programming with Python
# Brayan Gomez
# Mini project 1

import yfinance as yf


def get_closing(ticker_list):
    # get 10 day history of each stock
    hist = [yf.Ticker(stock).history(period="10d") for stock in ticker_list]

    closing_list = {}
    for i, stock in enumerate(hist):
        # closing for 10 days
        data = [f"{closing:.2f}" for closing in stock["Close"]]
        closing_list[ticker_list[i]] = data  # add entry

    return closing_list

stocks = ["META", "AMZN", "GOOG", "NFLX", "MSFT"]
print(get_closing(stocks))
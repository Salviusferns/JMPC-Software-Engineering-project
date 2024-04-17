import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500

def getDataPoint(quote):
    """Compute the correct stock price"""
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2  # Corrected calculation for stock price
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    """Calculate the ratio of two stock prices"""
    if price_b == 0:
        return None  # Avoid division by zero error
    return price_a / price_b

# Main
if __name__ == "__main__":
    prices = {}  # Dictionary to store stock prices
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
            prices[stock] = price  # Store the stock price in the prices dictionary
        # Calculate and print the correct ratio
        if 'ABC' in prices and 'DEF' in prices:
            ratio = getRatio(prices['ABC'], prices['DEF'])
            if ratio is not None:
                print("Ratio of two stock prices: %s" % ratio)

#!/usr/bin/env python3

import json
import urllib.request

URL = "https://api.iextrading.com/1.0/stock/{0}/quote"
CONFIG_FILE = './stocks.json'

# Getch a stock price
def get(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = response.read()

    return(data)


"""
Main
"""
def main():
    # Read the stocks config file
    fp = open(CONFIG_FILE, 'r')
    stocks = json.load(fp)
    fp.close()
    output = ''
    # Iterate through the stocks and get the prices
    for stock in stocks['stocks']:
        url = URL.format(stock)
        # If we can't fetch a stock price, mark it as 'N/A'
        try:	
            s = get(url).decode("utf-8")
            data = json.loads(s)
        except Exception:
            data = {}
            data['symbol'] = stock.upper()
            data['latestPrice'] = 'N/A'
            data['change'] = 'N/A'
            data['changePercent'] = 'N/A'
        # If not the first line add a newline
        if len(output) != 0:
            output += '\\n'
        # If the symbol is 'DIA' convert it from the ETF to the full DJIA stock price
        if data['symbol'] == 'DIA':
            data['symbol'] = 'DJIA'
            data['latestPrice'] = int(data['latestPrice'] * 100)
            data['change'] = int(data['change'] * 100)
        # If the symbol is 'SPY' convert it from the ETF to the full S&P 500 stock price
        if data['symbol'] == 'SPY':
            data['symbol'] = 'S&P'
            data['latestPrice'] = int(data['latestPrice'] * 10)
            data['change'] = int(data['change'] * 10)
        output += '{0} {1} {2}'.format(data['symbol'], data['latestPrice'], data['change'], int(data['changePercent'] * 1000) / 10)

    print(output)

# Main!
if __name__ == '__main__':
    main()

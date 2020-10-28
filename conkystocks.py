#!/usr/bin/env python3

import json
import urllib.request

DEBUG = False
URL = "https://cloud.iexapis.com/v1/stock/{0}/quote"
URL = "https://query1.finance.yahoo.com/v7/finance/quote?fields=regularMarketPrice&symbols={}"
URL = 'https://query1.finance.yahoo.com/v7/finance/quote?symbols={}'
CONFIG_FILE = './stocks.json'
CONVERT_FUNDS_TO_INDEXES = True


def get(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = response.read()

    return (data)


"""
Main
"""


def main():
    # Read config
    fp = open(CONFIG_FILE, 'r')
    stocks = json.load(fp)
    fp.close()
    output = []
    for stock in stocks['stocks']:
        url = URL.format(stock)
        try:
            s = get(url).decode("utf-8")
            data = json.loads(s)
        except Exception as e:
            data = {}
            data['symbol'] = stock.upper()
            data['latestPrice'] = 'N/A'
            data['change'] = 'N/A'
            data['changePercent'] = 0.0
        #if len(output) != 0:
        #    output += '\\n'
        data = data['quoteResponse']['result'][0]
        if CONVERT_FUNDS_TO_INDEXES:
            if data['symbol'] == 'DIA':
                data['symbol'] = 'DJIA'
                data['regularMarketPrice'] = int(data['regularMarketPrice'] * 100)
                data['regularMarketChange'] = int(data['regularMarketChange'] * 100)
            if data['symbol'] == 'SPY':
                data['symbol'] = 'S&P'
                data['regularMarketPrice'] = int(data['regularMarketPrice'] * 10)
                data['regularMarketChange'] = int(data['regularMarketChange'] * 10)
        output.append('{0} {1} {2} {3}%'.format(data['symbol'], data['regularMarketPrice'],
                                           int(data['regularMarketChange'] * 100) / 100,
                                           int(data['regularMarketChangePercent'] * 100) / 100))

    for line in output:
        print(line)


# Main!
if __name__ == '__main__':
    main()

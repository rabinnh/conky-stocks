#!/usr/bin/env python3

import json
import urllib.request

DEBUG = False
URL = "https://api.iextrading.com/1.0/stock/{0}/quote"
CONFIG_FILE = './stocks.json'
CONVERT_FUNDS_TO_INDEXES = False

def get(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = response.read()

    return(data)


"""
Main
"""
def main():
    # Read config
    fp = open(CONFIG_FILE, 'r')
    stocks = json.load(fp)
    fp.close()
    output = ''
    for stock in stocks['stocks']:
        url = URL.format(stock)
        try:	
            s = get(url).decode("utf-8")
            data = json.loads(s)
        except Exception:
            data = {}
            data['symbol'] = stock.upper()
            data['latestPrice'] = 'N/A'
            data['change'] = 'N/A'
            data['changePercent'] = '0/0'
        if len(output) != 0:
            output += '\\n'
        if CONVERT_FUNDS_TO_INDEXES:
            if data['symbol'] == 'DIA':
                data['symbol'] = 'DJIA'
                data['latestPrice'] = int(data['latestPrice'] * 100)
                data['change'] = int(data['change'] * 100)
            if data['symbol'] == 'SPY':
                data['symbol'] = 'S&P'
                data['latestPrice'] = int(data['latestPrice'] * 10)
                data['change'] = int(data['change'] * 10)
        output += '{0} {1} {2} {3}'.format(data['symbol'], data['latestPrice'], data['change'], int(data['changePercent'] * 1000) / 10)

    print(output)

# Main!
if __name__ == '__main__':
    main()

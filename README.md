# conky-stocks

This small project uses the api.iextrading.com stock API to fetch and retrieve stock prices for Conky

## Script

### Dependencies

As you can see, the script is named 'conkystocks.py' and should be placed in your $HOME/.conky directory.  It has been tested on Python 3.5 on Linux and
imports 'json' and 'urllib'.

### Market Indexes

As far as I can tell, api.iextrading.com does not support the Dow Jones Index or S&P 500.  However, it does support the related ETFs DIA and SPY.
For these two symbols conkystock.py will convert them to the approximate price and change of the indexes if the "CONVERT_FUNDS_TO_INDEXES" in
conkystocks.py is set to True.

## Configuration

To define which stocks are fetched, put your stock symbols in the stocks.json file in the JSON array, like so:

```
  {
    "stocks" : ["dia", "nvda", "jcap", "tsm", "msft", "fxf", "sds"]
  }
```

The stocks.json file should be colocated with comnystocks.py in your $HOME/.conky directory.

## To use in Conky

Typically used with execi like so:

```
  ${voffset 2}${color}${execi 30 echo $(./conkystocks.py)}
```  


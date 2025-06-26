import robin_stocks.robinhood as r # Import Robinhood API
from robin_stocks.robinhood import options # Import Options from Robinhood API
import threading # Import multi-threading

# ---===== || Functions || =====---

def fetchSharePrice(ticker):
    return r.stocks.get_latest_price(ticker, priceType=None, includeExtendedHours=False)

def fetchOptions(ticker, expireDate, optionType):
    pass
        
'''
    - Eventually incorporate multithreading to fetch API data faster
'''
        
    

    





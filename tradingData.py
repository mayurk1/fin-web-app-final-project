# Requires a config.py file containing the 
# below variables with alpaca account API keys
# and url
from config import api_key, api_secret, base_url
import alpaca_trade_api as tradeapi

# Instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

class histData: 
    def daily(ticker, delta):
        # Request historic data from alpaca API into
        # a pandas dataframe of daily closes delta 
        # days from current days (dataset has nontrading
        # days already removed) 
        stock = api.get_barset(ticker, 'day', limit=delta).df
        stock.columns = stock.columns.droplevel()

        return stock


    def min15(ticker, delta):
        # Request historic data from alpaca API into
        # a pandas dataframe
        stock = api.get_barset(ticker, 'minute', limit=delta).df
        stock.columns = stock.columns.droplevel()

        return stock

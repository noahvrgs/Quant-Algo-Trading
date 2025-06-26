import robin_stocks.robinhood as r
from robin_stocks.robinhood import options
from datetime import datetime
from dotenv import load_dotenv
import os

from fetch_options_data import fetchOptions, fetchSharePrice
from heston_model import hestonCall

# Robinhood Login w/ Account Credentials from .env
load_dotenv()
login = r.login(username = os.getenv("ROBINHOOD_USERNAME"), password = os.getenv("ROBINHOOD_PASSWORD"))
print("Login status:", login['detail'] if 'detail' in login else "Success!")

def main():
    print(fetchSharePrice("SOFI"))
    print(fetchOptions("SOFI", "2025-06-20", "call"))
    
if __name__=="__main__":
    main()
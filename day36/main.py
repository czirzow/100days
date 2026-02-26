import lib36.apijson as apijson


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# TODO: make this: apijson.ApiVantage(ApiJson): 
import os
import json
from datetime import datetime as dt, timedelta

## STEP 1: Use https://www.alphavantage.co
VANTAGE_API_KEY = os.environ.get('VANTAGE_API_KEY')
if not VANTAGE_API_KEY:
    raise Exception('need to export VANTAGE_API_KEY')

VANTAGE_API_ENDPOINT = 'https://www.alphavantage.co/query'

DATE_FORMAT = '%Y-%m-%d'

params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK,
        'apikey': VANTAGE_API_KEY,
        }

api = apijson.Request(VANTAGE_API_ENDPOINT)
data = api.call('', params)

cache_file = f"vantage-{STOCK}.json"
if not os.path.exists(cache_file):
    with open(cache_file, 'w') as fh:
        json.dump(data, fh, indent=4)
else:
    with open(cache_file, 'r') as fh:
        data = json.load(fh)

# {"date"}: {"awkward_names": "value" },
time_series = data['Time Series (Daily)']
""" {
        "2026-02-20": {
            "1. open": "255.1950",
            "2. high": "259.0400",
            "3. low": "253.8000",
            "4. close": "257.1600",
            "5. volume": "4708550"
        },
    }
"""
# We want the close values
close_key = '4. close'
# 
today = dt.now().strftime(DATE_FORMAT)
if today not in time_series:
    print(f"no data for: {today}")
    exit(1)

days = 1
while True:
    previous_day = (dt.now() - timedelta(days=days)).strftime(DATE_FORMAT)
    # Just in case the previous_day is a weekend or a holiday
    if previous_day in time_series:
        break
    else:
        """Market was closed"""
        pass
    days += days

# kind of trust the data with float() casting.

value_tdy = float(time_series[today][close_key])
value_prv = float(time_series[previous_day][close_key])

def get_percentage(v1, v2):
    return ((v2 - v1) / v1) * 100

print(today, value_tdy, value_prv, get_percentage(value_tdy, value_prv))





## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


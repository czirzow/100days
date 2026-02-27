import os
import json
import lib36.apijson as apijson
import steps.step1 as step1
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
TODAY='2026-02-26'
NUM_RESULTS = 3
SORT_BY = 'popularity'
NEWSAPI_API_KEY = os.environ.get('NEWSAPI_API_KEY')
NEWSAPI_ENDPOINT = 'https://newsapi.org/v2/'
if not NEWSAPI_API_KEY:
    raise Exception('need to export NEWSAPI_API_KEY=YourKey')

# request:
# https://newsapi.org/v2/everything
#     q=step1.COMPANY_NAME
#     from=today
#     sortBy=popularity
#     pageSize=3
#     apiKey=NEWSAPI_API_KEY
uri = 'everything'
params = {
        'q': step1.COMPANY_NAME,
        'from': TODAY,
        'sortBy': SORT_BY,
        'pageSize': NUM_RESULTS,
        'apiKey': NEWSAPI_API_KEY
        }

cache_name = 'newsapi'
exclude_keys = [NEWSAPI_API_KEY]
cache_key= ".".join([i for i in params.values() if i not in [NEWSAPI_API_KEY]])
cache_file = f"tmp/{cache_name}-{cache_key}.json"

if not os.path.exists(cache_file):
    api = apijson.Request(NEWSAPI_ENDPOINT)
    data = api.call(uri, params=params)
    with open(cache_file, 'w') as fh:
        json.dump(data, fh, indent=4)
else:
    with open(cache_file, 'r') as fh:
        data = json.load(fh)

#TODO: define a simple structure:
# headline
# brief
print(data)
exit(4)

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


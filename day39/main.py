# day 39

from flightlib.data_manager import DataManager
from flightlib.flight_search import FlightSearch
#from flightlib.notification_manager import NotificationManager
#from flightlib.flight_data import FlightData

#
# TODO: start testing this..
#   from lib39.apiclient import ApiClient
# it catches then throws common exceptions 
# in main code that uses ApiClient()
# 

import os
from dotenv import load_dotenv
from lib39.sheety import Sheety
from lib39.cache import Cache

__DEBUG__ = True
if __DEBUG__:
    from pprint import pprint


load_dotenv()
try: 
  sheety_key = os.environ['SHEETY_KEY']
except KeyError:
    raise Exception("Must setup environment sheety_key")




# WARNING: do not make the SHEET plural.
# For some reason, the api wants a singular word.
#   if sheet == prices
#   they want this as an update value on put and post requests
#       {'price': {field:value}}
#  makes no sense.
SHEET = 'price'
sheety = Sheety(key=sheety_key, project='flightDeals')
data_manager = DataManager(sheety)


# Avoid Calls to the api.
cache_sheety = Cache('tmp/cache_sheety_results.json')
if cache_sheety.is_cached():
    sheety_results = cache_sheety.get()
else:
    #API Call
    sheety_results = data_manager.get_sheet(SHEET)
    cache_sheety.save(sheety_results)
# call cache_sheety.clear() if data on sheety clears

# ensure that we have the iata codes set.
flight_search = FlightSearch()
for row in sheety_results[SHEET]:
    #pprint(row)
    if row['iataCode'] == '':
        code = flight_search.get_iata_code(row['city'])
        data_manager.put(SHEET, row['id'], {'iataCode': code})



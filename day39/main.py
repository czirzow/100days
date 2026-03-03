# day 39

from flightlib.data_manager import DataManager
#from flightlib.flight_data import FlightData
from flightlib.flight_search import FlightSearch
#from flightlib.notification_manager import NotificationManager

#from lib39.apirequest import ApiRequestJson
#this fails
#api = ApiRequestJson('http://google.com')
#api.get()

from dotenv import load_dotenv
import os
from pprint import pprint
from lib39.sheety import Sheety
from lib39.cache import Cache


load_dotenv()

try: 
  sheety_key = os.environ['SHEETY_KEY']
except KeyError:
    raise Exception("Must setup environment sheety_key")

sheety = Sheety(key=sheety_key, project='flightDeals')

# WARNING: do not make the SHEET plural.
# For some reason, the api wants a singular word.
#   sheetname == prices
# but the value to update a sheet needs to be this:
#    {'price': {field:value}}
#  makes no sense.
SHEET = 'price'

data_manager = DataManager(sheety)

# Avoid Calls to the api.
cache_sheety = Cache('tmp/cache_sheety_results.json')
if cache_sheety.is_cached():
    sheety_results = cache_sheety.get()
else:
    sheety_results = data_manager.get_sheet(SHEET)
    cache_sheety.save(sheety_results)

# ensure that we have the iata codes set.
flight_search = FlightSearch()
for row in sheety_results[SHEET]:
    #pprint(row)
    if row['iataCode'] == '':
        code = flight_search.get_iata_code(row['city'])
        data_manager.put(SHEET, row['id'], {'iataCode': code})


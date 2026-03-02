# day 39

#from flightlib.data_manager import DataManager
#from flightlib.flight_data import FlightData
#from flightlib.flight_search import FlightSearch
#from flightlib.notification_manager import NotificationManager

from lib39.apirequest import ApiRequestJson


#this fails
api = ApiRequestJson('http://google.com')
api.get()

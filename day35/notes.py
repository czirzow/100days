# notes day 35
import requests as req

# openweathermap.org
# apikey:

API_VERSION = '2.5'
API_ENDPOINT = f"https://api.openweathermap.org/data/{API_VERSION}/"
API_URI_WEATHER = 'weather'

API_KEY = 'c50f74019929a801e046f56ae0cb01ec'
MY_LAT = 38.439701 # Your latitude
MY_LON = -122.715637 # Your longitude

params = {
     'lat': MY_LAT,
     'lon': MY_LON,
     'appid': API_KEY,
     }

#class Cache
import json
#
class Cache():

     def __init__(self, name: str, cache_dir:str ='cache/'):
          self.name = API_URI_WEATHER
          self.cache_dir = cache_dir 

     def filename(self) -> str:
          return f"{self.cache_dir}{self.name}.json"

     def save(self, value: dict) -> bool:
          try:
               with open(self.filename(), 'w') as fh:
                   json.dump(value, fh, indent=4) 
          # TODO: add good handling here
          except FileNotFoundError:
               print("Error!")
               return False
          else:
               return True

     #still class Cache
     def read(self) -> dict:
          try: 
               with open(self.filename(), 'r') as fh:
                    data = json.load(fh);
          except FileNotFoundError as e:
               print("File not found"


          #open file and return a dict
          return data

     def is_cached(self) -> bool:
          return False
     def is_expired(self) -> bool:
          return False


## TODO: cache the value,
##      . if cache is not expired keep it otherwise do another request.
#url = f"{API_ENDPOINT}?lat={params['lat']}&lon={params['lon']}&appid={params['appid']}"
cache = Cache(API_URI_WEATHER)

if cache.is_cached():
     data = cache.read()
else:
     resp = req.get(API_ENDPOINT + API_URI_WEATHER, params=params)
     try:
         resp.raise_for_status()

     except req.exceptions.RequestException as e:
         print(f"Failed request: {e}")
         exit(1)
     data = resp.json()
     cache.save(data)





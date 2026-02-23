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
## def __init__(self, name: str, cache_dir:str ='cache/')
cache_dir = 'cache/'

def filename(name: str) -> str:
     return f"{cache_dir}{name}.json"

def save(name: str, value: str) -> bool:
     try:
          with open(filename(name), 'w') as fh:
              json.dump(value, fh, indent=4) 
     # TODO: add good handling here
     except FileNotFoundError:
          print("Error!")
          return False
     else:
          return True

#still class Cache
def read(name: str):
     pass
def is_cached(name: str):
     return False
def is_expired(name: str):
     pass


__TODO_CACHE_THIS__ = True
## TODO: cache the value,
##      . if cache is not expired keep it otherwise do another request.
#url = f"{API_ENDPOINT}?lat={params['lat']}&lon={params['lon']}&appid={params['appid']}"
if __TODO_CACHE_THIS__:
     resp = req.get(API_ENDPOINT + API_URI_WEATHER, params=params)
     try:
         resp.raise_for_status()

     except req.exceptions.RequestException as e:
         print(f"Failed request: {e}")
         exit(1)

     data = resp.json()
     print(data)
     print(save(API_URI_WEATHER, data))

else:
        pass







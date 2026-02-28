# just keeping this around for reference.
# This could be a tool for caching files for api calls.
import json
import os
class CacheJson():
     def __init__(self, name: str, cache_dir:str ='cache/'):
          self.name = name
          self.cache_dir = cache_dir 
          self.enabled = False

     def filename(self) -> str:
          return f"{self.cache_dir}{self.name}.json"

     
     def is_enabled(self):
          return self.enabled

     def save(self, value: dict) -> bool:
          try:
               with open(self.filename(), 'w') as fh:
                   json.dump(value, fh, indent=4) 
          # TODO: add good handling here
          except FileNotFoundError:
               return False
          else:
               return True

     #still class Cache
     def read(self) -> dict:
          try: 
               with open(self.filename(), 'r') as fh:
                    data = json.load(fh);
          except FileNotFoundError as e:
               print("File not found")
               return {}

          return data

     def is_cached(self) -> bool:
          return os.path.exists(self.filename())

     def is_expired(self) -> bool:
          #TODO:  enable this
          return False


import requests as req
class Request():
    def __init__(self, api_endpoint):
         self.api_endpoint = api_endpoint

    def call(self, uri, params):
          resp = req.get(self.api_endpoint + uri, params=params)
          try:
              resp.raise_for_status()

          except req.exceptions.RequestException as e:
              print(f"Failed request: {e}")
              exit(1)

          return resp.json()



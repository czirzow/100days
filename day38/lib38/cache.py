import json, os

class Cache:
    """Simple method to cache dict results in a file"""

    def __init__(self, cache_file:str):
        self.cache_file = cache_file

    def is_cached(self) -> bool:
        return os.path.exists(self.cache_file)

    def get(self) -> dict:
        with open(self.cache_file, 'r') as fp:
            return json.load(fp)

    def save(self,  results:dict) -> None:
        with open(self.cache_file, 'w') as fp:
            json.dump(fp=fp, obj=results, indent=4)



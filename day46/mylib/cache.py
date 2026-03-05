import json, os

class Cache:
    """Simple method to cache dict results in a file"""

    def __init__(self, cache_file:str):
        self.cache_file = cache_file

    def is_cached(self) -> bool:
        return os.path.exists(self.cache_file)

    def clear(self):
        """clears the cache"""
        if self.is_cached():
            os.remove(self.cache_file)

class CacheFile(Cache):
    """Just save the contents to a file"""

    def get(self) -> str:
        with open(self.cache_file, 'r') as fp:
            return fp.read()

    def save(self, data) -> None:
        with open(self.cache_file, 'w') as fp:
            fp.write(data)


# untested
class CacheJson(Cache):
    """Use json to save the file"""

    def get(self) -> dict:
        with open(self.cache_file, 'r') as fp:
            return json.load(fp)

    def save(self,  results:dict) -> None:
        with open(self.cache_file, 'w') as fp:
            json.dump(fp=fp, obj=results, indent=4)



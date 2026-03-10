import json, os
from typing import Callable

class Cache:
    """Simple method to cache dict results in a file"""

    def __init__(self, cache_file:str, callback: Callable):
        self.cache_file = cache_file
        self.callback = callback

    def is_cached(self) -> bool:
        return os.path.exists(self.cache_file)

    def _get_callback(self):
         return self.callback()

    def clear(self):
        """clears the cache"""
        if self.is_cached():
            os.remove(self.cache_file)

class CacheFile(Cache):
    """Just save the contents to a file"""

    def get(self) -> str:
        with open(self.cache_file, 'r') as fp:
            return fp.read()

    def _save(self, data) -> None:
        with open(self.cache_file, 'w') as fp:
            fp.write(data)


# untested
class CacheJson(Cache):
    """Use json to save the file"""

    def get(self) -> dict:
        if  self.is_cached():
            print("cached", self.cache_file)
            with open(self.cache_file, 'r') as fp:
                results = json.load(fp)
            return results
        else:
            results = self._get_callback()
            print("results:", type(results))
            self._save(results)
            print(results)
            return results


    def _save(self,  results) -> None:
        with open(self.cache_file, 'w') as fp:
            json.dump(fp=fp, obj=results, indent=4)



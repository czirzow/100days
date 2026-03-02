#filename: apirequests.py

import requests as req
class ApiRequest():

    def __init__(self):
        pass

    def _request(self, method, url:str, params:dict, headers:dict) -> dict:
        resp = method(url, params=params, headers=headers)
        try:
            resp.raise_for_status()

        # TODO: are there specific exceptions i would like to catch? and not exit
        except req.exceptions.RequestException as e:
            print(f"Failed request: {e}")
            exit(1)

        try:
            return resp.json()
        except ValueError as e:
            raise Exception(f"Result was not json: {e}")

    def get(self, url: str, params: dict | None = None, headers: dict | None = None) -> dict:
        return self._request(req.get, url, params or {}, headers or {})

    def post(self, url: str, params: dict | None = None, headers: dict | None = None) -> dict:
        return self._request(req.post, url, params or {}, headers or {})

    def put(self, url: str, params: dict | None = None, headers: dict | None = None) -> dict:
        return self._request(req.put, url, params or {}, headers or {})

    def delete(self, url: str, params: dict | None = None, headers: dict | None = None) -> dict:
        return self._request(req.delete, url, params or {}, headers or {})

__TEST__ = True
if __TEST__:
    api = ApiRequest()
    print(api)


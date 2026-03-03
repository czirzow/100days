#filename: apirequests.py

##
# This seems like a lot of work to just handle what happens
# in a requests.request() call
# perhaps... I should do some research on a good library..
# Found it... stand by, a rewrite is comming shortly.

import requests as req

class ApiRequstError(Exception):
    pass

class ApiRequestErrorJson(ApiRequstError):
    pass

class ApiRequestJson():

    def __init__(self, url):
        self.url = url

    def _request(self, method, params:dict, headers:dict) -> dict:
        try:
            resp = method(self.url, params=params, headers=headers)
            resp.raise_for_status()

        # TODO: are there specific exceptions i would like to catch?
        except req.exceptions.RequestException as e:
            raise ApiRequstError(f"Failed request: {e}")

        try:
            return resp.json()
        except ValueError as e:
            raise ApiRequestErrorJson(f"Result was not json: {e}")

    def get(self, params: dict | None = None, headers: dict | None = None) -> dict:
        """requests.get(url, params=None, **kwargs)"""
        return self._request(req.get, params or {}, headers or {})

    def post(self, params: dict | None = None, headers: dict | None = None) -> dict:
        """requests.post(url, data=None, json=None, **kwargs)"""
        return self._request(req.post, params or {}, headers or {})

    def put(self,  params: dict | None = None, headers: dict | None = None) -> dict:
        """requests.put(url, data=None, **kwargs)"""
        return self._request(req.put, params or {}, headers or {})

    def delete(self, params: dict | None = None, headers: dict | None = None) -> dict:
        """requests.delete(url, **kwargs)"""
        return self._request(req.delete, params or {}, headers or {})


__TEST__ = False
__test_for__ = None
#__test__ = 'basic-init-fail'
if __TEST__:
    if __test_for__ == None:
        pass
    if __test_for__ == 'basic-init-fail':
        #passed
        api = ApiRequestJson('https://google.com/')
        try:
            resp = api.get()
        except ApiRequstError as e:
            print(f"we failed as expected {e}")


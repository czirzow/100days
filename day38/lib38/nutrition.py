import requests

NUTRITION_API_BASE = "https://app.100daysofpython.dev"

class ApiNutrition:
    def __init__(self, app_id:str, app_key:str):
        self.app_id = app_id
        self.app_key = app_key
    
    def url_exersize(self) -> str:
        return NUTRITION_API_BASE + "/v1/nutrition/natural/exercise"

    def url_healthz(self) -> str:
        return NUTRITION_API_BASE + "/healthz"

    def auth_headers(self) -> dict:
        return {
                'x-app-id': self.app_id,
                'x-app-key': self.app_key,
                }

    def _request(self, url, json={}) -> dict:
        resp = requests.get(url=url, json=json,
                            headers=self.auth_headers())
        try:
              resp.raise_for_status()
        except requests.exceptions.RequestException as e:
              print(f"Failed request: {e}")
              exit(1)
        return resp.json()

    def _post(self, url, json={}) -> dict:
        resp = requests.post(url=url, json=json,
                            headers=self.auth_headers())
        try:
              resp.raise_for_status()
        except requests.exceptions.RequestException as e:
              print(f"Failed request: {e}")
              exit(1)

        return resp.json()
     
    def exersize(self, activity:str) -> dict:
        params = {
                'query': activity,
                }
        return self._post(url=self.url_exersize(), json=params)

    def healthz(self) -> dict:
        return self._request(url=self.url_healthz())


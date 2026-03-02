import requests

SHEETY_BASE_URL = "https://api.sheety.co"
class Sheety:
    def __init__(self, key:str, project: str):
        self.key = key
        self.project = project

    def _url_with_key(self) -> str:
        return SHEETY_BASE_URL + f"/{self.key}"

    def url(self, sheet:str) -> str:
        return self._url_with_key() + f"/{self.project}/{sheet}"

    def get(self, sheet:str):
        return requests.get(url=self.url(sheet)).json()

    def add(self, sheet:str, workout:dict):
        url = self.url(sheet)
        json = { 'workout': workout }
        resp = requests.post(url=url, json=json)
        try:
              resp.raise_for_status()
        except requests.exceptions.RequestException as e:
              print(f"Failed request: {e}")
              exit(1)
        return resp.json()

    def update(self, sheet:str, id:int, workout:dict):
        url = self.url(sheet) + f"/{id}"
        json = { 'workout': workout }
        resp = requests.put(url=url, json=json)
        try:
              resp.raise_for_status()
        except requests.exceptions.RequestException as e:
              print(f"Failed request: {e}")
              exit(1)
        return resp.json()


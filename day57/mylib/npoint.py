
from mylib.apiclient import ApiClient

class Npoint():
    url = 'https://api.npoint.io/'
    def __init__(self, id:str = 'c790b4d5cab58020d391'):
        self.api = ApiClient(self.url + id)

    def get_records(self):
        return self.api.get('/').json()

    def get_record(self, id):
        return [b for b in self.get_records() if b['id'] == id][0]


from mylib.apiclient import ApiClient

class Guess:
    def __init__(self, name):
        self.name = name
        self.api_age = ApiClient('https://api.agify.io')
        self.api_gender = ApiClient('https://api.genderize.io')

    def guess_age(self):
        return self.api_age.get('/', params={'name': self.name}).json()['age']

    def guess_gender(self):
        return self.api_gender.get('/', params={'name': self.name}).json()['gender']


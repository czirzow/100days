import requests as req

API_ENDPOINT = 'https://opentdb.com/api.php'

class OpenTriviaApi:
    """Retrieve questions from Open Trivia Api"""

    def __init__(self, amount=10, type='boolean', category=0):
        self.amount = amount
        self.type = type
        self.category = category

    def get(self):
        pass

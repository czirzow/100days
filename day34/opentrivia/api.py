import requests as req
import html

API_ENDPOINT = 'https://opentdb.com/api.php'

class OpenTriviaApi:
    """Retrieve questions from Open Trivia Api"""

    def __init__(self, amount=10, answer_type='boolean', category=0):
        self.amount = amount
        self.answer_type = answer_type
        self.category = category

    def get_params(self):
        params = {}
        
        if self.amount < 1:
            self.amount = 10
        params['amount'] = self.amount
        
        if self.answer_type:
            params['type'] = self.answer_type

        return params

    def get(self):
        resp = req.get(API_ENDPOINT, self.get_params())
        try:
            resp.raise_for_status()

        except req.exceptions.RequestException as e:
            print(f"Failed api call: {e}")
            return {}

        data = resp.json()
        if data['response_code'] != 0:
            print("error getting content: code[{data['response_code']}")
            return {}

        # using default encoding html codes
        # lets clean it up.
        for item in data['result']:
            q = item.get('question')
            if isinstance(q, str):
                item['question'] = html.unescape(q)

        return data['results']


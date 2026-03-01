
# is there a better way?
from datetime import datetime as dt
class Workout:
    def __init__(self):
        #self.id:int = 0         # row number
        self.date:str = ''
        self.time:str = ''
        self.exercise:str = ''
        self.duration:int = 0
        self.calories:int = 0

    def _get_date(self):
        return dt.now().strftime('%d/%m/%Y')

    def _get_time(self):
         return dt.now().strftime('%H:%M:%S')

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() 
                if not k.startswith('_')}

    def from_exercise(self, exercise:dict):
        self.date = self._get_date()
        self.time = self._get_time()
        self.exercise = exercise['name'].capitalize()
        self.duration = exercise['duration_min']
        self.calories = exercise['nf_calories']


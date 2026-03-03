from lib39.sheety import Sheety

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, sheety:Sheety):
        self.sheety = sheety

    def get_sheet(self, sheet):
        return self.sheety.get(sheet)

    def put(self, sheet:str, id:int, values:dict):
        self.sheety.update(sheet, id, values)





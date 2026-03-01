# day 
import os
from lib38.nutrition import ApiNutrition


sheety_key = os.environ.get('sheety_key')
app_key = os.environ.get('nutrition_app_key')
app_id = os.environ.get('nutrition_app_id')
if not (app_key and app_id and sheety_key):
    raise Exception("Must setup environment for app_key and app_id and sheety_key")

api = ApiNutrition(app_id=app_id, app_key=app_key)

if api.healthz()['status'] != 'ok':
    print("Api not up")
    exit(1)

#from pprint import pprint
#pprint(api.exersize('swam for 1 hour'))





# day 
import json, os
from lib38.nutrition import ApiNutrition
from lib38.sheety import Sheety
from lib38.workout import Workout
from lib38.cache import Cache

from pprint import pprint

sheety_key = os.environ.get('sheety_key')
app_key = os.environ.get('nutrition_app_key')
app_id = os.environ.get('nutrition_app_id')
if not (app_key and app_id and sheety_key):
    raise Exception("Must setup environment for app_key and app_id and sheety_key")

nutrition = ApiNutrition(app_id=app_id, app_key=app_key)

if False:
    """disable for now"""
    if nutrition.healthz()['status'] != 'ok':
        print(f"Api not up: {api.url_healthz()}")
        exit(1)


# avoid hitting the api while testing.
cache = Cache('tmp/cache_nutrition_results.json')
if cache.is_cached():
    nutrition_results = cache.get()
else:
    nutrition_results = nutrition.exercise('swam for 1 hour')
    cache.save(nutrition_results)


workout = Workout()
for exercise in nutrition_results['exercises']:
    workout.from_exercise(exercise)
    pprint(workout.to_dict())


sheety = Sheety(key=sheety_key, project='curtWorkouts')
#print(sheety.url())

cache = Cache('tmp/cache_sheety_results.json')
if cache.is_cached():
    sheety_results = cache.get()
else:
    sheety_results = sheety.get('workouts')
    cache.save(sheety_results)

for row in sheety_results['workouts']:
    pprint(row)




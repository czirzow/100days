# day 
import os
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

# avoid hitting the api while testing.
cache_sheety = Cache('tmp/cache_sheety_results.json')

nutrition = ApiNutrition(app_id=app_id, app_key=app_key)
sheety = Sheety(key=sheety_key, project='curtWorkouts')

if False:
    """disable for now"""
    if nutrition.healthz()['status'] != 'ok':
        print(f"Api not up: {api.url_healthz()}")
        exit(1)

if False:
    """Testing adding a new record"""
    cache = Cache('tmp/cache_nutrition_results.json')
    if cache.is_cached():
        nutrition_results = cache.get()
    else:
        nutrition_results = nutrition.exercise('swam for 1 hour')
        cache.save(nutrition_results)

    workout = Workout()
    for exercise in nutrition_results['exercises']:
        workout.from_exercise(exercise)
        # TODO: add entry to sheety and clear cache_sheety
        sheety.add('workouts', workout.to_dict())
        cache_sheety.clear()

if False:
    """test the update of an item"""
    workout = {
            'id': 2,
            'calories': 326,
            'date': '01/03/2026',
            'duration': 60,
            'exercise': 'Swimming',
            'time': '17:24:05'
            }
    sheety.update('workouts', workout['id'], workout)
    cache_sheety.clear()

if False:
    """test delete an item"""
    print(sheety.delete('workouts', 2))
    cache_sheety.clear()


if cache_sheety.is_cached():
    sheety_results = cache_sheety.get()
else:
    sheety_results = sheety.get('workouts')
    cache_sheety.save(sheety_results)

for row in sheety_results['workouts']:
    pprint(row)





### Overview 
  * Focused on creating classes in a lib that are independent.
      * [Sheety()](lib38/sheety.py) - API to [sheety.co](https://sheety.co)
      * [ApiNutrition()](lib38/nutrition.py) - API to [Nutrition and Exercise API](https://app.100daysofpython.dev/services/nutrition/docs)
      * [Workout()](lib38/workout.py) - a dict helper.
  * Re-thought a simple [Cache](lib38/cache.py) class to avoid hitting the api to test run.
    * Adds the ability to see the data scructure of the result to 
      better understand it in the context of your data.
  * [main.py](main.py) ended up being a unit test like setup.


### setup environment
```
cat > my_env
    export nutrition_app_id=YOUR_GENERATED_ID
    export nutrition_app_key=YOUR_GENERATED_KEY
    export sheety_key=KEY_FROM_SHEETY
source ./my_env
```




# notes
import requests as r
import time as t


iss_api = 'http://api.open-notify.org/iss-now.json'

if 0:
    # to avoid many calls
    response = r.get(url=iss_api)
    response.raise_for_status()
    data_iss_postion = response.json().get('iss_position')

data_iss_position =  {'longitude': '-148.9484', 'latitude': '28.5944'}

iss_position = (data_iss_position['longitude'], data_iss_position['latitude'])
print(iss_position)

import requests as req
from datetime import datetime
from lib33.latlon import haversine


MY_LAT =  38.439701 # Your latitude
MY_LONG =  -122.715637 # Your longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    'tzid': 'America/Los_Angeles',
}

__CALL_APIS__ = False


if __CALL_APIS__:
    # just so we don't keep call the api 
    response = req.get("https://api.sunrise-sunset.org/json", params=parameters)
    try: 
        response.raise_for_status()
    except req.exceptions.RequestException as e:
        print("Unable to get sunrise/sunset: {e}")
        exit(1)

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_hour = datetime.now().hour
    #if  not (current_hour > sunset and current_hour < sunrise):
        #print("It is day time")
        #exit()

print("Looking for ISS ...")


if __CALL_APIS__:
    response = req.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)
else:
    iss_latitude = 17.9751
    iss_longitude = 55.7115

#Your position is within +5 or -5 degrees of the ISS position.
distance = haversine(MY_LAT, MY_LONG, iss_latitude, iss_longitude)
if distance <= 2100:
    print(f"ISS is {distance:,.1f} km away... you may be able to see it.")
else:
    print(f"ISS is {distance:,.1f} km away... way to far")






#If the ISS is close to my current position

# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




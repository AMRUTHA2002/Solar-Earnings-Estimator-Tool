import math
import pickle
from pysolar.solar import get_altitude
import datetime
import requests
import numpy as np
from datetime import datetime
from meteostat import Point, Monthly
import pytz
from geopy.geocoders import Nominatim
import sklearn


def get_city_name(lat, lon):
    # create the locator
    geolocator = Nominatim(user_agent="SolarPredictor")

    # getting the location address
    location = geolocator.reverse(str(lat) + ", " + str(lon))
    # >>> result : Backwerk, Potsdamer Platz, Tiergarten, Mitte, Berlin, 10785, Deutschland

    # getting address compontent like street, city, state, country, country code, postalcode and so on.
    location.raw.get('address').get('state')
    #print(location.raw.get('address').get('city'))
    return location.raw.get('address').get('city')
    location.raw.get('address').get('country')
    location.raw.get('address').get('postcode')


# todo: update requirements
def predict_power(distance, temperature, wspd, sky, visibility, humidity, ensemble_stack):
    x = np.zeros(6)
    x[0] = distance
    x[1] = temperature
    x[2] = wspd
    x[3] = sky
    x[4] = visibility
    x[5] = humidity

    return ensemble_stack.predict([x])[0]


def setup(lat: float, lon: float):
    start = datetime(2022, 1, 1)
    end = datetime(2022, 12, 31)
    print(lat, lon)
    tpr = Point(lat, lon)

    data = Monthly(tpr, start, end)
    data = data.fetch()
    print(data)

    if len(data) != 0:
        celsius = (sum(data['tavg'])) / len(data)
    else:
        celsius = 15

    temperature = (celsius * 1.8) + 32

    if len(data) != 0:
        wspd = (sum(data['wspd'])) / len(data)
    else:
        wspd = 65

    t = 0
    latitude = lat
    longitude = lon
    for i in range(0, 12):
        date = datetime(2022, i + 1, 1, 12, 0, 0, 0, pytz.UTC)
        d = get_altitude(latitude, longitude, date)
        t += math.radians(d)
    distance = t / 12
    # print("The distance to solar moon is ", distance)

    apiKey = "d5f6e96071109af97ee3b206fe8cb0cb"
    baseURL = "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
    cityName = get_city_name(lat, lon)
    print("City name", cityName)
    # print(cityName)
    #completeURL = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}"
    completeURL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}"
    response = requests.get(completeURL)
    print(response)
    data = response.json()
    # print(data)

    v = data["visibility"]
    visibility = v / 1000

    humidity = data["main"]["humidity"]
    c = data["weather"][0]["description"]

    if c == "broken clouds":
        sky = 2
    elif c == "scattered clouds":
        sky = 1
    elif c == "sky clear" or c == "few clouds":
        sky = 0
    elif c == "overcast clouds":
        sky = 4
    else:
        sky = 4

    # patch_sklearn()

    objects = []
    with (open("ml/trained_model.sav", "rb")) as file:
        ensemble_stack = pickle.load(file)
        # ensemble_stack = None
    return distance, temperature, wspd, sky, visibility, humidity, ensemble_stack


def calculate_savings(lat: float, lon: float) -> float:
    distance, temperature, wspd, sky, visibility, humidity, ensemble_stack = setup(lat, lon)
    return predict_power(distance, temperature, wspd, sky, visibility, humidity, ensemble_stack)

import random
import requests
# ny = source_places[0]
# print ny[0]
# print ny[1]


BASE_URL_Forecast_10day = 'http://api.wunderground.com/api/63577728b0e9ae1f/forecast10day/q/'

def get_api_url_forecast(state, city):
    city = city.replace(" ", "_")
    return "{}/{}/{}.json".format(BASE_URL_Forecast_10day, state, city)

def forecast(state, city):
	url = get_api_url_forecast(state, city)
	r = requests.get(url)
	j = r.json()
	days = j['forecast']['txt_forecast']['forecastday']

	for day in days:
	    print city, "--", day['title'], ": ", day['fcttext']
	    icon = day['icon']
	    if "rain" in icon:
	    	print icon, " bring an umbrella!"

def random_places():
	(city, state) = random_places()
	source_places = [('New York', 'NY'), ('San Francisco', 'CA'), ('Seattle', 'WA'), ('Houston', 'TX')]
	random_location = random.choice(source_places)
	print random_location

def random_weather_forecast():
	weather_place = get_api_url_forecast(random_places)
	the_weather = forecast(weather_place)
	print the_weather

random_weather_forecast()

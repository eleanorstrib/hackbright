import random
import requests
#source_places = [('New York', 'NY'), ('San Francisco', 'CA'), ('Seattle', 'WA'), ('Houston', 'TX')]
# ny = source_places[0]
# print ny[0]
# print ny[1]

BASE_URL_Forecast_10day = 'http://api.wunderground.com/api/63577728b0e9ae1f/forecast10day/q/'
source_places = [('New York', 'NY'), ('San Francisco', 'CA'), ('Seattle', 'WA'), ('Houston', 'TX'), ]


	
def get_api_url_forecast(state, city):
	#formats forecast data from API to be used in def forecast function
    city = city.replace(" ", "_")
    return "{}/{}/{}.json".format(BASE_URL_Forecast_10day, state, city)

def forecast(state, city):
	#calls api to get forecast data from Underground Weather API
	url = get_api_url_forecast(state, city)
	r = requests.get(url)
	j = r.json()
	days = j['forecast']['txt_forecast']['forecastday']

	for day in days:
	#loops through data for specific city to pull day and forecast, with added feature to let you know if it's raining'''
	    return "In {} on {}, the weather will be {}".format(city, day['title'], day['fcttext'])
	    icon = day['icon'] 
	    if "rain" in icon:
	    	return "it may rain on {}, don't forget to bring an umbrella".format(day['title'])

def random_location():
#selects a random state-city pair and splits tuple into separate variables of city and state 
	
	random_place = random.choice(source_places)
	state = random_place[1]
	city = random_place[0]
	return (state, city)
	


def random_weather_forecast(state, city):
	'''applies random city choice to the forecast functions
	to generate the weather report for the randomly chosen city'''
	the_weather = forecast(state, city)
	print the_weather

(state, city) = random_location()
random_weather_forecast(state, city)

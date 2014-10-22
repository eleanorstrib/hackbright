import random
import requests
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACfd28ac16c257b7849021fd7b008997fd"
auth_token = "47e3fb75cea6054f3db2779a98cb313d"
client = TwilioRestClient(account_sid, auth_token)

(city, state) = get_random_place_name()
the_weather = weather(city, state)
success = text_this(my_phone_number, message, test_mode)

BASE_URL_Forecast_10day = 'http://api.wunderground.com/api/63577728b0e9ae1f/forecast10day/q/'

	
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
	    print city, "--", day['title'], ": ", day['fcttext']
	    icon = day['icon'] 
	    if "rain" in icon:
	    	print "\n", icon, " bring an umbrella!"



#def random_weather_forecast(state, city):
'''applies random city choice to the forecast functions
to generate the weather report for the randomly chosen city'''
source_places = [('New York', 'NY'), ('San Francisco', 'CA'), ('Seattle', 'WA'), ('Houston', 'TX')]
random_place = random.choice(source_places)
state = random_place[1]
city = random_place[0]
weather_at_location = get_api_url_forecast(state, city)
the_weather = forecast(state, city)
print the_weather

#it works just as is now, but i broke it when i wrapped in in function?


def text_this(number, message, test=False):
	#sends a message to the number supplied
	if test:
		print "This would have sent a SMS to {}. Message: {}".format(number, message)
		return True
	else:

	message = client.messages.create(to=number"The weather in {}, {} is {}".format(city, state, the_weather)
	my_phone_number ="+12698158889" # "Send to" phone number
	from_ ="+19252593131" # Twilio number sent from
	test_mode = True #change to False to send a text
	
	#returns True if the message sent OK
	
	def generate_message():
		

	#and False if there was an exception
	if test = False:

    # ... send SMS code here...
    print message.sid
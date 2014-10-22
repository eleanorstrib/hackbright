from twilio.rest import TwilioRestClient
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACfd28ac16c257b7849021fd7b008997fd"
auth_token = "47e3fb75cea6054f3db2779a98cb313d"
client = TwilioRestClient(account_sid, auth_token)

#from more_weather import random_weather_forecast

number ="+15102201256"


def generate_message():
	message = "Duck! Watch Out! Melissa is messing with code;\
	 Now she's playing with with twilio.She apologizes in advance."
	return message


def text_this(number, message, test=False):
	#sends a message to the number supplied
	message = client.messages.create(body=message, to=number, # Replace phone number
	from_="+19252593131") # Replace Twilio number
	return message
	print message.sid

message = generate_message()
text_this(number, message)
from twilio.rest import TwilioRestClient
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACfd28ac16c257b7849021fd7b008997fd"
auth_token = "47e3fb75cea6054f3db2779a98cb313d"
client = TwilioRestClient(account_sid, auth_token)
message = client.messages.create(body="Jenny please?! I love you <3",
to="+12698158889", # Replace phone number
from_="+19252593131") # Replace Twilio number
print message.sid

def text_this(number, message, test=False):
	#sends a message to the number supplied
	message = client.messages.create(body="Jenny please?! I love you <3",
	to="+12698158889", # "Send to" phone number
	from_="+19252593131") # Twilio number
	
	#returns True if the message sent OK
	if test = True:
		print "This would have sent a SMS to {}. Message: {}".format(number, message)

	#and False if there was an exception
	if test = False:



    # ... send SMS code here...
    print message.sid
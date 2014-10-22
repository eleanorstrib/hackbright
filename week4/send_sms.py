from twilio.rest import TwilioRestClient
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACfd28ac16c257b7849021fd7b008997fd"
auth_token = "47e3fb75cea6054f3db2779a98cb313d"
client = TwilioRestClient(account_sid, auth_token)

number =15102201256
def text_this(number, message, test=False):
	#sends a message to the number supplied
	message = client.messages.create(body="Duck! Watch Out! Melissa is messing with code; Now she's playing with with twilio. \
		She apologizes in advance!",
	to="+15102201256", # Replace phone number
	from_="+19252593131") # Replace Twilio number
	

	#returns True if the message sent OK
	# if test:
	# 	print "This would have sent a SMS to {}. Message: {}".format(number, message)
	# 	return True

	# #and False if there was an exception
	# if test:
	#  = False:



    # ... send SMS code here...
text_this(number, message)
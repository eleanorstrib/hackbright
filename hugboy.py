HUGBOT_NAME = 'henrietta'

#speak("Hello, my name is " + HUGBOT_NAME)

def speak(message):
	print message

def hug():
	speak("**hug**")

def boot():
	speak("0101010101110110111000000.... Ready")
	speak("Hello, my name is " + HUGBOT_NAME)

def get_name():
    return HUGBOT_NAME

def brain():
	boot()
	hug()

brain()

#speak("Hello, my name is " + HUGBOT_NAME)

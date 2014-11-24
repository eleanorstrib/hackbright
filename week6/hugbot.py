import random

HUGBOT_NAME = 'henrietta'
#boot_options = [True, False]
hugbot_actions = ['hug', 'wave', 'sleep', 'dance']

action_map = { 'dance': "...(^-^)...~\(*-*)/~...\(^-^)/ ...",
				'hug': "**hug**",
				'wave': "**wave**",
				'sleep':"soooo sleepy...(-.-)Zzz...",
}

#speak("Hello, my name is " + HUGBOT_NAME)

def speak(message):
	print message



def get_name():
    return HUGBOT_NAME

# def hug():
# 	speak("**hug**")
# 	return True

# def wave():
# 	speak("**wave**")
# 	return True

# def sleep():
# 	speak("soooo sleepy...(-.-)Zzz...")
# 	return True

# def dance():
# 	speak("...(^-^)...~\(*-*)/~...\(^-^)/ ...") 
# 	return True
def perform_action():
		return

	


def boot():
	bot_name=get_name()
	speak("010101010111011011100000.... Steady...Steady...Ready!")
	speak("Hello, my name is " + bot_name)

	say_my_name = raw_input("Say my name, Say my name...Ain't callin' me baby.Better say my name:")
	if say_my_name == 'henrietta' or 'Henrietta':
		return bot_name
	else:
		return False

	# random_outcome = random.choice(boot_options)
	# return random_outcome

def brain():
	booted_ok = boot()
	if booted_ok:
		#action = random.choice(hugbot_actions)
		while True:
			action = raw_input("What should Hugbot do: hug, wave, sleep, dance, or quit?")
			if action == 'hug':
				hug()
			if action == 'wave':
				wave()
			if action == 'sleep':
				sleep()
			if action == 'dance':
				dance()
			if action == 'quit':
				return
	else:
		speak("System failure :(")


# def perform_action():
# 	if hug = True:
# 		perform_action('hug') => "Henrietta Hugs"
# 	if wave = True:
# 		perform_action('wave') => "Henrietta Waves"
# 	if sleep = True:
# 		preform_action('sleep') => "Henrietta Sleeps"


brain()

#speak("Hello, my name is " + HUGBOT_NAME)

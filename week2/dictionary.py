leet_skillz = {
    'halo': 10,
    'starcraft': 4,
    'hearthstone': 7,
    'solitaire': 11,
    'simcity': 9
    }

print leet_skillz['simcity']

awesome = leet_skillz.get('halo')
oops = leet_skillz.get('callofduty')

print awesome
print oops

# best_game_ever = "dominion"
# leet_skillz[best_game_ever] = 4

# print leet_skillz

# for game in leet_skillz:
# 		print "looking at {}".format(game)
# 		skill = leet_skillz[game]
		

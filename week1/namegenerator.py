>>>
import random


 
first_name_list = []
last_name_list = []
		
	


def name_generator():

	for name in data:
	...     name_pieces = name.strip().split(" ")
		print name_pieces

	...     first_name = name_pieces[0]
	...     last_name = name_pieces[1]
	...     print first_name
	...     print last_name

		first_name_list.append(first_name)
		last_name_list.append(last_name)


	random_first_name = random.choice(first_name_list)
	random_last_name = random.choice(last_name_list)

	if first_name == last_name:
		print "the things are the same things"
		
	print random_first_name + " " + random_last_name

name_generator()





	

	




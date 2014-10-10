import csv
import sys

print sys.argv[0]

try:
	my_street = sys.argv[1] 
except:
	print "i need a street name"
	exit()

print my_street


def sweep_times(street_name):
	with open('sweep.csv') as f:
		my_reader = csv.reader(f)


		for row in my_reader:
			if row[5].lower() == street_name.lower():
				
				print "The left side of the {} block of ".format(row[14:16]) + street_name \
					+ " is swept on {}".format(row[1]) + " between the times of {}".format(row[6:8])

				print "The right side of the {} block of ".format(row[16:18]) + street_name \
					+ " is swept on {}".format(row[1]) + " between the times of {}".format(row[6:8])
			
sweep_times(my_street)


#

# def  print_hello(name):
# 	print "Hello, {name}".format(name=name)

# print_hello("Lady Gaga")
# print_hello("Benedict Cumberbatch")


# def many_things(one, two, three, four, five, six):
#     print "I have one {one}, two {two}s, three {three}s, four {four}s, five {five}s and six {six}s.".format(one=one, two=two, three=three, four=four, five=five, six=six)

# many_things("nose", "ear", "piercing", "limb", "sense", "cousin")
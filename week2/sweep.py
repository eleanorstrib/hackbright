import csv

neighborhoods = []
monday = 0
tuesday = 0
wedensday = 0
thursday = 0
friday = 0


with open('sweep.csv') as f:
	my_reader = csv.reader(f)
	for row in my_reader:
		neighborhood = row[-2]
		if neighborhood not in neighborhoods:
			neighborhoods.append(neighborhood)

		if row[1] == "Mon":
			monday += 1
		if row[1] == "Tues":
			tuesday += 1
		if row[1] == "Wed":
			wedensday += 1
		if row[1] == "Thu":
			thursday += 1
		if row[1] == "Fri":
			friday += 1

		if row[5] == "Sutter St":
			
			print "The left side of the {} block of Sutter Street".format(row[14:16]) \
				+ " is swept on {}".format(row[1]) + " between the times of {}".format(row[6:8])

			print "The right side of the {} block of Sutter Street".format(row[16:18]) \
				+ " is swept on {}".format(row[1]) + " between the times of {}".format(row[6:8])
			

			"""
		left_from = row[14]
		left_to = row[15]
		if left_from == '301' and left_to == '399':
			print 'They are the same'
		"""
		# try:
		# 	left_from = int(row[14])
		# 	left_to = int(row[15])

		# except:
		# 	print "this row has some wierd data! Boo!"
		# 	continue

		# if left_from < 400 and left_to > 300:
		# 		print "I am on my block"






print "Found {} neighborhoods".format(len(neighborhoods))
print sorted(neighborhoods) 

print "On mondays, SF is swept ", monday, "times"
print "On tuesday, SF is swept ", tuesday, "times"
print "On wedensday, SF is swept ", wedensday, "times"
print "On thursday, SF is swept", thursday, "times"
print "On friday, SF is swept", friday, "times"


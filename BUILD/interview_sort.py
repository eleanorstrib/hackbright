import csv
import time
from datetime import datetime

tutors = {
'Samantha Rocha': {'Mon': (100, 600),
					'Tue': (0, 0),
					'Wed': (100, 600),
					'Thu': (100, 300),
					'Fri': (0, 0)
					}
		}


Emerson_Berkeley = {
	'Mon': (200, 400),
	'Tue': (200, 400),
	'Wed': (200, 400),
	'Thu': (200, 400),
	'Fri': (100, 245)

}

Jefferson = {
	'Mon': (230, 430),
	'Tue': (0, 0),
	'Wed': (230, 430),
	'Thu': (0, 0),
	'Fri': (230, 430)
}
# weekdays = ["Monday", "Tuesday", "Wedensday", "Thursday", "Friday"]



def tutors_who_travel():
	#loops through data to search for tutors who are willing to travel to oakland & who have cars
	with open('BUILD_DataTest.csv') as f:
		tutors = csv.DictReader(f)
		print tutors.next()

		
		for tutor in tutors:
			# if tutor['Willing to Travel?'] == "Yes":
			# 	oakland_tutors = {}
			# 	oakland_tutors = tutor['Last Name'], tutor['First Name'], 

			# 	print oakland_tutors

			if tutor['Monday Start Time'] != "Not Available":
				monday_tutors = {}
				monday_tutors = tutor['Last Name'], tutor['First Name'], 
				monday_times = {}
				monday_times = tutor['Monday Start Time'], tutor['Monday End Time']
				print monday_times
				
				print "{} can work on Monday between {} - {} ".format(monday_tutors, tutor['Monday Start Time'], tutor['Monday End Time'])



			


#selects oakland sites
def oakland_site_finder():
	with open('BUILD_SiteTimes.csv') as g:
		site_times = csv.DictReader(g)

		for site in site_times:
			if site['city'] == "Oakland":
				print site['site_name'], site['Monday Start Time'], site['Monday End Time']
			print site_times.next()



def Berkeley_Arts_Magnet():
	BAM = {
		'Mon': (315, 500),
		'Tue': (315, 500),
		'Wed': (315, 500),
		'Thu': (315, 500),
		'Fri': (0, 0)	
		}
	
	print xrange(BAM['Mon'][0])
	print tutors.fromkeys()


	
	
def main():
	print "Welcome to BUILD's Sort-o-Matic!"

	oakland_site_finder()
	tutors_who_travel()
	Berkeley_Arts_Magnet()
    


if __name__=="__main__":
    main()

# with open('BUILD_SiteTimes.csv') as d:
#     build = csv.DictReader(d)
#     for site_name in build:
#         print site_name
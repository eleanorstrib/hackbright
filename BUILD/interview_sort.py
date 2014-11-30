import csv
import time
from datetime import datetime

days = ["Monday", "Tuesday", "Wedensday", "Thursday", "Friday"]



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
			site_avail = {}
			if site['city'] == "Oakland":
				print site['site_name'], site['Monday Start Time'], site['Monday End Time']
			print site_times.next()


def Berkeley_Arts_Magnet():
	with open('BUILD_SiteTimes2.csv') as g:
		site_times = csv.Reader(g)
		BAM_avail = {}		
		for site from site_times
			start_time = []
			start_time = list.site['Mond']
			BAM_avail = dict.fromkeys(days)

	print xrange(BAM['Mon'][0])
	print tutors.fromkeys()


	
	
def main():
	print "Welcome to BUILD's Sort-o-Matic!"

	
	Berkeley_Arts_Magnet()
    


if __name__=="__main__":
    main()h
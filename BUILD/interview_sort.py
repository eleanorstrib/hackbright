import csv
import time
from datetime import datetime

oakland_site_match_list = []
berkeley_site_match_list = []
unmatched_tutors_list = []


def tutors_who_travel():
	#loops through data to search for tutors who are willing to travel to oakland
	with open('BUILD_DataTest.csv') as f:
		my_reader = csv.reader(f)

		for row in my_reader:
			if row[22] == "Yes":
				traveling_tutors = row[1] + ", " + row[0]
				traveling_tutors_list = []
				traveling_tutors_list.append(traveling_tutors)
				return traveling_tutors_list

				if row[22] =="Yes" and row[21] =="Yes":
					tutors_with_car_access = row[1] + ", " + row[0]
					tutors_with_car_access_list = []
					tutors_with_car_access_list.append(tutors_with_car_access)
					return tutors_with_car_access_list
					print "{} has car access and is willing to travel".format(tutors_with_car_access_list)

			if row[21] =="Yes" and row[22] =="No":
				tutors_with_car_access = row[1] + ", " + row[0]
				tutors_with_car_access_list = []
				tutors_with_car_access_list.append(tutors_with_car_access)
				print "{} has car access but s/he does not want to travel".format(tutors_with_car_access_list)
				

tutors_who_travel()


"""  	
#compares workstudy/credit tutors's availability with site's times to check tutor 
can work at least 2 days on site.
def workstudy_credit_tutors():

	for row in my_reader:
		if row[16] == "Work-study":
			
			create dictionary of tutors availability
			 tutor_availabilty = []


			for row in site_times:
				create dictionary of site's availability
				site_hours = []

				if tutor_availabilty == site_hours:
					tutor_matches_site = 0
					tutor_matches_site += 1

					if tutor_matches_site >= 2:
						print row[0] + " " + row[1], "qualifies for workstudy or credit hours at" row[0]/[site name]

					if tutor_matches_site < 2:
						print row[0] + " " + row[1],  "qualifies for volunteer status"

workstudy_tutors()
"""


#selects oakland sites
def oakland_site_finder():
	with open('BUILD_SiteTimes.csv') as g:
		site_times = csv.reader(g)

		for row in site_times:
			if row[1] == "Oakland":		
				oakland_sites = row[0]
				oakland_sites_list = []
				oakland_sites_list.append(oakland_sites)
				print oakland_sites_list

oakland_site_finder()

"""
compares tutor preferences availability with site's times

	for row in my_reader:
		#create dictionary of tutors availability
			 tutor_availabilty = {}

		#create list of tutor preferences
			tutor_preferences = {}


		for row in site_times:
				#create dictionary of site's availability
				site_hours = {}

		if tutor_preferences row[17:20] = True:

			for tutor_preferences in site_hours:

					if tutor_preferences row[17:20] == site && tutor_availabilty == site_times:
						return 


tutor_preferences_match()

"""	

"""
compares tutor_availabilty & site availability

			create list of tutors availability
			 tutor_availabilty = []


			for row in site_times:
				create dictionary of site's availability
				site_hours = []

			if tutor_availabilty = site_hours


			else tutor_availabilty != site_hours:
				unmatched_tutors_list.append(tutor)





"""

# with open('BUILD_SiteTimes.csv') as d:
#     build = csv.DictReader(d)
#     for site_name in build:
#         print site_name
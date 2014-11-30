import csv
from operator import itemgetter

days = ["Monday", "Tuesday", "Wedensday", "Thursday", "Friday"]


def Prospective_Tutors():
	"""collects tutors availability schedules from csv, 
	creates tuples of day, start/end time ranges"""
	with open('BUILD_DataTest2.csv') as f1:
		tutors = csv.DictReader(f1)
		fn = tutors.fieldnames
		print fn
		print tutors.next()
		tutor_avail = {}

		for tutor in tutors:
			tutor_start = []
			tutor_start.extend([tutor["Monday Start Time"], tutor["Tuesday Start Time"], tutor["Wednesday Start Time"], tutor["Thursday Start Time"], tutor["Friday Start Time"]])
			
			tutor_end = []
			tutor_end.extend([tutor["Monday End Time"], tutor["Tuesday End Time"], tutor["Wednesday End Time"], tutor["Thursday End Time"], tutor["Friday End Time"]])
			tutor_day_times = zip(days, map(strtime_to_minutes,tutor_start), map(strtime_to_minutes,tutor_end ))

			
			tutor_avail[tutor['Last Name']] = tutor_day_times
			#print tutor_avail


		return tutor_avail


def BUILD_sites():
	"""collects site availability schedules from csv file, 
	creates tuples of day, start/end time ranges in minutes"""
	with open('BUILD_SiteTimes2.csv') as f2:
		site_times = csv.DictReader(f2)
		
		site_avail = {}
		
		for site in site_times:

			site_start = []
			site_start.extend([site["Monday Start Time"], site["Tuesday Start Time"], site["Wednesday Start Time"], site["Thursday Start Time"], site["Friday Start Time"]])
			
			site_end = []
			site_end.extend([site["Monday End Time"], site["Tuesday End Time"], site["Wednesday End Time"], site["Thursday End Time"], site["Friday End Time"]])
			
			site_day_times = (zip(days, map(strtime_to_minutes, site_start), map(strtime_to_minutes, site_end)))

			
			site_avail[site['site_name']] = site_day_times

	#print site_avail
	return site_avail

def strtime_to_minutes(strtime):
	"""convert time as 24-hour clock string to minutes"""
	parts = strtime.split(':')
	l = len(parts)
	if l == 2 or l==3 : 
		return int(parts[0])*60 + int(parts[1])
	else:
		return -1

# print strtime_to_minutes("10:30")
# print strtime_to_minutes("blah")

def overlap(interval1, interval2):
	"""find time overlaps between tutor and sites"""
	day1, start_inter1, end_inter1 = interval1
	day2, start_inter2, end_inter2 = interval2
	overlap = max(0,min(end_inter1,end_inter2)- max(start_inter1,start_inter2))
	return overlap

	# x = range(start_inter1, end_inter1)
	# y = range(start_inter2, end_inter2)
	# set_x = set(x)
	# set_y = set(y)
	# intersect = set_x.intersection(set_y)
	# overlap = len(intersect)

	# return overlap
	# print overlap


#print overlap(('Monday', 815, 1000), ('Monday', 915, 1050))



def total_overlap(schedule1, schedule2):
	"""return total overlap between two schedules"""
	total = 0
	#print schedule1
	for day1, day2 in zip(schedule1, schedule2):
		#print day1, day2
		t = overlap(day1, day2)
		if t < 60: t = 0
		total += t
	return total






	# if take_overlap >= 60:
	# 	hours_overlap = divmod(take_overlap, 60)
	# 	hours, minutes = hours_overlap

	# 	print "XXXX can work {} hour(s) and {} minutes on {}".format(hours, minutes)
	# if take_overlap < 60:
	# 	print "XXXX does not have enough availability for site x"
	# else:
	# 	return


def main():
	print "Welcome to BUILD's Sort-o-Matic!"
	tutor_avail = Prospective_Tutors()
	site_avail = BUILD_sites()
	print tutor_avail

	for site, site_schedule in site_avail.items():
		times = []
		for tutor, tutor_schedule in tutor_avail.items():
			#print tutor, " : ", site, " : ", total_overlap(tutor_schedule, site_schedule)
			t = total_overlap(tutor_schedule, site_schedule)
			times.append((tutor, t))
		print times
		stimes = sorted(times, key=itemgetter(1), reverse=True)
		print site, stimes


if __name__=="__main__":
    main()
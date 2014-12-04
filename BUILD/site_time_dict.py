import csv
from operator import itemgetter
from flask import Flask, render_template, request, jsonify

# Include the Dropbox SDK
import dropbox



# app = Flask(__name__) # Initialize the app. launches server.


#Flask functions
# @app.route('/')
# def hello_world():
#     return "Welcome to BUILD's Sort-o-matic!"

# def shutdown_server():
#     func = request.environ.get('werkzeug.server.shutdown')
#     if func is None:
#         raise RuntimeError('Not running with the Werkzeug Server')
#     func()

# @app.route('/shutdown', methods=['POST'])
# def shutdown():
#     shutdown_server()
#     return 'Server shutting down...'

#Sort-o-Matic's functions

days = ["Monday", "Tuesday", "Wedensday", "Thursday", "Friday"]

def prospective_tutors():
	"""collects tutors availability schedules from csv,
	creates tuples of day, start/end time ranges"""
	with open('BUILD_DataTest2.csv') as f1:
		tutors = csv.DictReader(f1)
#fn = tutors.fieldnames
		tutor_avail = {}
		
		for tutor in tutors:
			tutor_start = []
			tutor_start.extend([tutor["Monday Start Time"], tutor["Tuesday Start Time"], tutor["Wednesday Start Time"], tutor["Thursday Start Time"], tutor["Friday Start Time"]])
			tutor_end = []
			tutor_end.extend([tutor["Monday End Time"], tutor["Tuesday End Time"], tutor["Wednesday End Time"], tutor["Thursday End Time"], tutor["Friday End Time"]])
			tutor_day_times = zip(days, map(strtime_to_minutes,tutor_start), map(strtime_to_minutes,tutor_end ))		
			
			if tutor['Willing to Travel?'] == "Yes":
				tutor_avail[(tutor['Last Name'] + ", " + tutor['First Name']), "**WtT"] = tutor_day_times
				if tutor["Access to Car"] == "Yes":
					tutor_avail[(tutor['Last Name'] + ", " + tutor['First Name']), "**WtT +Car"] = tutor_day_times
			elif tutor["Access to Car"] == "Yes":
				tutor_avail[(tutor['Last Name'] + ", " + tutor['First Name']), "+Car"] = tutor_day_times
			else:
				tutor_avail[(tutor['Last Name'] + "," + tutor['First Name'])] = tutor_day_times

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
		
		return site_avail

def strtime_to_minutes(strtime):
	"""convert time as 24-hour clock string to minutes"""
	parts = strtime.split(':')
	l = len(parts)
	if l == 2 or l==3 : 
		return int(parts[0])*60 + int(parts[1])
	else:
		return -1


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



def total_overlap(schedule1, schedule2):
	"""return total overlap between two schedules"""
	total = 0
	#print schedule1
	for day1, day2 in zip(schedule1, schedule2):
		#print day1, day2
		t = overlap(day1, day2)
		if t < 60: 
			t = 0
		total += t
	return total


def sorting_sites(site_avail,tutor_avail):
	"""compares site schedules against tutors' schedules"""
	stimes_list = []
	
	for tutor, tutor_schedule in tutor_avail.items():
		#tutor_name = str.join(last_name, first_name)
		tutor_dict = {}
		tutor_dict['name'] = tutor
		for site, site_schedule in site_avail.items():
			t = total_overlap(tutor_schedule, site_schedule)
		
			if t > 60: 
				tutor_dict[site] = t
			
		#stimes = sorted(times, key=itemgetter(1), reverse=True)
		stimes_list.append(tutor_dict)

		print tutor_dict

		#print site, ": ", stimes
	return stimes_list

def output_csv(stimes):
	"""outputs sorted sites as csv file"""

	#file_name = raw_input("save file as?")
	key = stimes[0].keys()
	key.remove("name")
	key.insert(0, "name")

	with open('pre_sort.csv', "wb") as f3:
		writer = csv.writer(f3, delimiter=',')
		writer.writerow(key)

		for row in stimes:
			t = []
			for k in key:
				minutes = row.get(k, 0)
				t.append(minutes)

	
			# name, hour, minutes = t
			# print "{} hour(s) and {} minutes".format(hour, minutes)

			writer.writerow(t)

		#writer.close()

def dropbox():
#Get your app key and secret from the Dropbox developer website
	app_key = 'pxb85nvmkunftb2'
	app_secret = 'jls2d3kb3dt1lmj'

	flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
	authorize_url = flow.start()

	print '1. Go to: ' + authorize_url
	print '2. Click "Allow" (you might have to log in first)'
	print '3. Copy the authorization code.'
	code = raw_input("Enter the authorization code here: ").strip()

	# This will fail if the user enters an invalid authorization code
	access_token, user_id = flow.finish(code)

	client = dropbox.client.DropboxClient(access_token)
	print 'linked account: ', client.account_info()

	f = open('pre_sort.csv', 'rb')
	response = client.put_file('/pre_sorted_tutors.csv', f)
	print 'uploaded: ', response

	folder_metadata = client.metadata('/')
	print 'metadata: ', folder_metadata

	f, metadata = client.get_file_and_metadata('pre_sorted_tutors.csv')
	out = open('pre_sorted_tutors.csv', 'wb')
	out.write(f.read())
	out.close()
	print metadata



def main():
	
	print "Welcome to BUILD's Sort-o-Matic!"
	tutor_avail = prospective_tutors()
	site_avail = BUILD_sites()

	stimes_list = sorting_sites(site_avail, tutor_avail)
	output_csv(stimes_list)
	#app.run(debug=True)
	dropbox()

if __name__=="__main__":

    main()

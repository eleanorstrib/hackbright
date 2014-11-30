site = {'Young Adult Project': [('Monday', 930, 1020), ('Tuesday', 930, 1020), ('Wedensday', 930, 1020), ('Thursday', 930, 1020), ('Friday', -1, -1)]}
tutor = {'Meraz': [('Monday', -1, -1), ('Tuesday', 780, 960), ('Wedensday', 780, 1080), ('Thursday', 780, 1080), ('Friday', -1, -1)]}


def overlap(interval1, interval2):
	"""find time overlaps between tutor and sites"""
	day, start_inter1, end_inter1 = interval1
	day, start_inter2, end_inter2 = interval2
	x = range(start_inter1, end_inter1)
	y = range(start_inter2, end_inter2)
	set_x = set(x)
	set_y = set(y)
	intersect = set_x.intersection(set_y)
	overlap = len(intersect)

	return overlap
	print overlap


#('Monday', 815, 1000), ('Monday', 915, 1050)



def total_overlap(schedule1, schedule2):
	"""totals overlap across the week days and across sites"""
	

	
	print overlap(schedule1, schedule2)

def main():
	print "Welcome to BUILD's Sort-o-Matic!"

	
if __name__=="__main__":
    main()
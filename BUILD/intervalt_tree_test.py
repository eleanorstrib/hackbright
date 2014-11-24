from intervaltree import Interval, IntervalTree
import csv






def oakland_site_finder():
	with open('BUILD_SiteTimes.csv') as g:
		site_times = csv.DictReader(g)
		for sites in site_times:
			print sites

def main():
	print "Welcome to BUILD's Sort-o-Matic!"

	oakland_site_finder()



if __name__=="__main__":
    main()



# intervals = [[100, 200], [150, 250], [300, 400], [250, 500], [100, 150], [175, 250]]
# intervals.sort()
# l = len(intervals)
# overlaps = []
# for i in xrange(l):
#   for j in xrange(i+1, l):
#     x = intervals[i]
#     y = intervals[j]
#     if x[0] == y[0]:
#       overlaps.append([x, y])
#     elif x[1] == y[1]:
#       overlaps.append([x, y])
#     elif (x[1]>y[0] and x[0]<y[0]):
#       overlaps.append([x, y])
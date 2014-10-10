import csv


with open('BUILD_DataTest.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print row
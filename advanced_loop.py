import os
os.chdir('c:/mymodules/csv')

with open('csv.csv') as file_data:
    print(file_data.read())

#another method (using builtin csv module's reader function which return a list of each line )

import csv
with open('csv.csv') as data:
    for line in csv.reader(data):
        print(line)
#Each line of raw data is being
#read from the file, then magically turned into a number of header item of list.

#Reading csv as dictionaries

with open('csv.csv') as data:
    for line in csv.DictReader(data):
        print(line)

with open('csv.csv') as file:
    ignore = file.readline()
    students = {}
    list1 = []
    for line in file :
        k,v = line.strip().split(',')
        if k in students:
            list1.append(v)
            students[k] = list1
        else:
            students[k] = v
print(students)

import pprint
pprint.pprint(students)

#Convert the destinations from UPPERCASE to Titlecase sample

string_upper = "I DID NOT MEAN TO SHOUT"
string_title = string_upper.title()
print(string_upper)
print(string_title)

#Convert the flight times from 24-hour format to AM/PM format

from datetime import datetime
def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')
with open('time.csv') as data:
    ignore = data.readline()
    students= {}
    for line in data:
        k,v = line.strip().split(',')
        students[k] = v
pprint.pprint(students)
print()
students2 = {}
for k, v in students.items():
    students2[convert2ampm(k)] = v.title()
pprint.pprint(students2) 

#converting patterns into Comprehensions

more_dest = []
more_dest = [dest.title() for dest in students2.values()]
fts2 = [convert2ampm(ft) for ft in students2.keys()]

#specifying dictionary comphresion

more_flights = {convert2ampm(k): v.title() for k, v in students.items()}

#Extend Comprehensions with Filters
just_freeport2 = {convert2ampm(k): v.title() for k, v in flights.items() if v == 'FREEPORT'}

import csv
import os

def slots(filename, courseCode):
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, '', 'Courses.csv')

    with open(path) as  data:
        slot = csv.reader(data, delimiter=',')
        for row in slot:
            if (row[0] == courseCode) :
                return row

def handle(req):
    slotsLst = slots('Courses.csv', req)
    slotsLstString = ""
    for s in slotsLst:
        slotsLstString = slotsLstString + "+" + s
    return slotsLstString

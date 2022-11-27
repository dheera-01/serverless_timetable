import csv
import os
import re
import requests

arr = ['A1','A2','A3','B1','B2','B3','C1','C2','C3','D1','D2','D3','E1','E2','E3','F1','F2','F3','G1','G2','G3','H1','H2','H3','I1','I2','I3','T1','T2','T3','K1','K2','K3','M1','M2','M3','N1','N2','N3','R1','R2','R3','P1','P2','J1','J2','L1','L2']

def courses(filename, input):
    list = []
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, '', filename)

    with open(path) as  data:
        course = csv.reader(data, delimiter=',')
        next(course)
        for row in course:
            if (row[0] == input) :
                list.append(row)
                break
        return list
 
def fun(slot , list, arr):
    for i in range(0, 48):
        if (arr[i] == slot):
            return list[i+1]
 
def fetch(Roll, slot):
    new_list = courses('TT.csv', Roll)
    ans = fun(slot, new_list[0], arr)
    return ans

def getCourseSlots(courseCode):
    slotsString = requests.get("http://gateway.openfaas:8080/function/getslots",data=courseCode).text
    slots = slotsString.split('+')
    return slots

def appendRollCourses(slots, roll, courseCode):
    new_list=[]

    for i in arr:
        if i in slots:
            new_list.append(courseCode)
        else:
            new_list.append('')

    return new_list

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    command = req[0]
    
    if(command == 'N'):
        # Call function to create new entry
        flag = 0
        for i in range(len(req)):
            if (req[i] == '$'):
                flag = i
                break
        rollnum = req[1:i]
        courses_string = req[i+2:len(req)]

        my_courses = re.split(r'[+]', courses_string)

        temp_list = []
        for i in arr:
            temp_list.append('')

        for courseCode in my_courses:
            if courseCode != '':
                new_row = appendRollCourses(getCourseSlots(courseCode),rollnum,courseCode)
                for i in range(0,len(temp_list)):
                    if new_row[i] != '':
                        if temp_list[i] != '':
                            temp_list[i] = temp_list[i] + "+" + new_row[i]
                        else:
                            temp_list[i] = temp_list[i] + new_row[i]

        temp_list.insert(0,rollnum)
        print(temp_list)
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, '', 'TT.csv')
        with open(path, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(temp_list)
            csvfile.close()
        return "SUCCESS"
    elif command == 'C':
        rollnum = req[1:]
        checkList = courses('TT.csv',rollnum)
        if len(checkList) == 0:
            return "NO"
        return "YES"
    else:
        # Call function to get course code for slot
        rollno,slot = req.split("$")
        rtr = fetch(rollno,slot)
        if rtr == None:
            return ""
        return rtr

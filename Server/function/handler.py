import csv
import os
import re

arr = ['A1','A2','A3','B1','B2','B3','C1','C2','C3','D1','D2','D3','E1','E2','E3','F1','F2','F3','G1','G2','G3','H1','H2','H3','I1','I2','I3','T1','T2','T3','K1','K2','K3','M1','M2','M3','N1','N2','N3','R1','R2','R3','P1','P2','J1','J2','L1','L2']

#---------ServerGETSLOTS
def slots(filename, courseCode):
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, '', 'Courses.csv')

    with open(path) as  data:
        slot = csv.reader(data, delimiter=',')
        # next(slot)
        for row in slot:
            if (row[0] == courseCode) :
                return row

def ServerGETSLOTS(req):
    slotsLst = slots('Courses.csv', req)
    slotsLstString = ""
    for s in slotsLst:
        slotsLstString = slotsLstString + "+" + s
    return slotsLstString


#---------ServerFETCH
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
    # print(new_list)
    ans = fun(slot, new_list[0], arr)
    return ans

def getCourseSlots(courseCode):
    slotsString = ServerGETSLOTS(courseCode)
    # slotsString = "+CS304+G1+G2+G3+*+*"
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

def ServerFETCH(req):
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
                # print(new_row)
                # print(len(temp_list))
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

#---------ServerTIMETABLE
def requests_get(req):
    return ServerFETCH(req)
 
def ServerTIMETABLE(req):
   """handle a request to the function
   Args:
       req (str): request body
   """
 
   A1 = requests_get(req+"$A1")
   A2 = requests_get(req+"$A2")
   A3 = requests_get(req+"$A3")
 
   B1 = requests_get(req+"$B1")
   B2 = requests_get(req+"$B2")
   B3 = requests_get(req+"$B3")

   C1 = requests_get(req+"$C1")
   C2 = requests_get(req+"$C2")
   C3 = requests_get(req+"$C3")

   D1 = requests_get(req+"$D1")
   D2 = requests_get(req+"$D2")
   D3 = requests_get(req+"$D3")
 
   E1 = requests_get(req+"$E1")
   E2 = requests_get(req+"$E2")
   E3 = requests_get(req+"$E3")
 
   F1 = requests_get(req+"$F1")
   F2 = requests_get(req+"$F2")
   F3 = requests_get(req+"$F3")
 
   G1 = requests_get(req+"$G1")
   G2 = requests_get(req+"$G2")
   G3 = requests_get(req+"$G3")
 
   H1 = requests_get(req+"$H1")
   H2 = requests_get(req+"$H2")
   H3 = requests_get(req+"$H3")
 
   I1 = requests_get(req+"$I1")
   I2 = requests_get(req+"$I2")
   I3 = requests_get(req+"$I3")
 
   T1 = requests_get(req+"$T1")
   T2 = requests_get(req+"$T2")
   T3 = requests_get(req+"$T3")
 
   K1 = requests_get(req+"$K1")
   K2 = requests_get(req+"$K2")
   K3 = requests_get(req+"$K3")
 
   M1 = requests_get(req+"$M1")
   M2 = requests_get(req+"$M2")
   M3 = requests_get(req+"$M3")
 
   N1 = requests_get(req+"$N1")
   N2 = requests_get(req+"$N2")
   N3 = requests_get(req+"$N3")
 
   R1 = requests_get(req+"$R1")
   R2 = requests_get(req+"$R2")
   R3 = requests_get(req+"$R3")
 
   P1 = requests_get(req+"$P1")
   P2 = requests_get(req+"$P2")
 
   J1 = requests_get(req+"$J1")
   J2 = requests_get(req+"$J2")
 
   L1 = requests_get(req+"$L1")
   L2 = requests_get(req+"$L2")

   page_html = '''
   <!DOCTYPE html>
       <html>
       <style>
           table, th, td {
           border:1px solid black;
           }
       </style>
       <body>
 
           <h2>Timetable:</h2>
 
           <table style="width:100%">
           <tr>
               <td></td>
               <td>Monday</td>
               <td>Tuesday</td>
               <td>Wednesday</td>
               <td>Thursday</td>
               <td>Friday</td>
           </tr>
 
           <tr>
               <td>8:05-9:00</td>
               <td>'''+A1+'''</td>
               <td>'''+B2+'''</td>
               <td>'''+A2+'''</td>
               <td>'''+B3+'''</td>
               <td>'''+A3+'''</td>
           </tr>
 
           <tr>
               <td>9:05-10:00</td>
               <td>'''+B1+'''</td>
               <td>'''+C1+'''</td>
               <td>'''+D2+'''</td>
               <td>'''+C2+'''</td>
               <td>'''+C3+'''</td>
           </tr>
 
           <tr>
               <td>10:05-11:00</td>
               <td>'''+D1+'''</td>
               <td>'''+E1+'''</td>
               <td>'''+E2+'''</td>
               <td>'''+D3+'''</td>
               <td>'''+E3+'''</td>
           </tr>
 
           <tr>
               <td>11:05-12:00</td>
               <td>'''+G1+'''</td>
               <td>'''+F1+'''</td>
               <td>'''+F2+'''</td>
               <td>'''+G3+'''</td>
               <td>'''+F3+'''</td>
           </tr>
 
           <tr>
               <td>12:05-13:00</td>
               <td>'''+H1+'''</td>
               <td>'''+H2+'''</td>
               <td>'''+G2+'''</td>
               <td>'''+I3+'''</td>
               <td>'''+H3+'''</td>
           </tr>
 
           <tr>
               <td>13:05-14:00</td>
               <td>'''+I1+'''</td>
               <td>'''+I2+'''</td>
               <td>'''+T1+'''</td>
               <td>'''+T2+'''</td>
               <td>'''+T3+'''</td>
           </tr>
 
           <tr>
               <td>14:05-14:30</td>
               <td rowspan="2">'''+K1+'''</td>
               <td rowspan="3">'''+J1+'''</td>
               <td rowspan="2">'''+K2+'''</td>
               <td rowspan="2">'''+K3+'''</td>
               <td rowspan="3">'''+J2+'''</td>
           </tr>
 
           <tr>
               <td>14:35-15:00</td>
           </tr>
 
           <tr>
               <td>15:05-15:30</td>
               <td rowspan="2">'''+M1+'''</td>
               <td rowspan="2">'''+M2+'''</td>
               <td rowspan="2">'''+M3+'''</td>
           </tr>
 
           <tr>
               <td>15:35-16:00</td>
               <td rowspan="3">'''+L1+'''</td>
               <td rowspan="3">'''+L2+'''</td>
           </tr>
 
           <tr>
               <td>16:05-16:30</td>
               <td rowspan="2">'''+N1+'''</td>
               <td rowspan="2">'''+N2+'''</td>
               <td rowspan="2">'''+N3+'''</td>
           </tr>
 
           <tr>
               <td>16:35-17:00</td>
           </tr>
 
           <tr>
               <td>17:05-18:00</td>
               <td>'''+P1+'''</td>
               <td>'''+R1+'''</td>
               <td>'''+P2+'''</td>
               <td>'''+R2+'''</td>
               <td>'''+R3+'''</td>
           </tr>
          
           </table>
 
 
       </body>
   </html>
   '''
   return page_html


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    print(req)

    command = req[0]
    if command == 'N':
        return ServerFETCH(req)

    rollnum = 'C' + req
    existCheck = ServerFETCH(rollnum)
    if existCheck == "YES":
        return ServerTIMETABLE(req)
    else:
        return "NO"

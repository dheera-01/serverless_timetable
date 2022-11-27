import requests

def download(html_string):
    fp = open("timetable.html", 'w')
    fp.write(html_string)
    fp.close()

roll_no = input("Enter your rollno.: ")
front_rtr = requests.get("http://localhost:5000/",data=roll_no).text

if front_rtr == "NO":
    print("User doesn't exist. Enter courses: ")
    courses_list = ""
    course = "N" + roll_no + "$"
    courses_list += course
    while course != "":
        course = input()
        courses_list = courses_list + "+" +course
    print(courses_list)
    fetch_rtr = requests.get("http://localhost:5000/",data=courses_list).text

front_rtr = requests.get("http://localhost:5000/",data=roll_no).text
download(front_rtr)
print("Timetable downloaded as timetable.html.")
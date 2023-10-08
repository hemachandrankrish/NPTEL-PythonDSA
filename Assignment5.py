def getDatawithOptions():
    inputFlag = 1
    if inputFlag == 1:
            dataFile = open("/Users/hemachandrankrishnan/dsprojects/Python-DSA/Assignment5.1-Data","r")
            #dataFile = open(filename,"r")
            inputData = dataFile.read()
            inputData = inputData.split('\n')
    else:
        while(True):
            try:
                stdInputData = input()
                inputData = inputData+stdInputData+'\n'
                if stdInputData == "EndOfInput":
                    break
            except ValueError:
                print("error in inputs")
            except EOFError:
                break
        print(inputData)
        inputData = inputData.split('\n')
    return inputData

def getData():
    inputData = ""
    while(True):
        try:
            stdInputData = input()
            inputData = inputData+stdInputData+'\n'
            if stdInputData == "EndOfInput":
                break
        except ValueError:
            print("error in inputs")
        except EOFError:
            break
    inputData = inputData.split('\n')
    return inputData

def StudentGrades():
    inputData =  getDatawithOptions() 
    iCourses, iStudents, iGrades = [], [], [] #Inputs
    keyCheck = ""
    for inputlines in inputData:
        if inputlines.strip() == "Courses" or inputlines.strip() == "Students" or inputlines.strip() == "Grades":
            keyCheck = inputlines.strip()
        elif inputlines.strip() == "EndOfInput":
            break
        if keyCheck == "Courses" and inputlines.strip() != "Courses":
            iCourses.append(inputlines)
        elif keyCheck == "Students" and inputlines.strip() != "Students":
            iStudents .append(inputlines)
        elif keyCheck == "Grades" and inputlines.strip() != "Grades":
            iGrades.append(inputlines)
    print(iGrades)
    gradeDict = {"A":10,"AB":9,"B":8,"BC":7,"C":6,"CD":5,"D":4} #dictionary of marks
    #grades_to_points = {'A': 10, 'AB': 9, 'B': 8, 'BC': 7, 'C': 6, 'CD': 5, 'D': 4}
    studentAvgTotal = []
    for student in iStudents:
        student = student.split('~')
        coursecount,studentAvg,spclKey = 0,0,0
        for grade in iGrades:
            grade = grade.split('~')
            if student[0] == grade[3]:
                coursecount += 1
                studentAvg += gradeDict[grade[4]]
                #studentAvg = round(studentAvg/coursecount,2)
            # if student[0] == grade[3] and student[0]=="RAV4301" :
            #     coursecount += 1
            #     spclKey = 1
            #     studentAvg += gradeDict[grade[4]]
        #if student[0]=="RAV4301" and spclKey ==1:
        studentAvg = 0 if coursecount ==0 else round(studentAvg/coursecount,2)
        #studentAvgTotal = studentAvgTotal+[str(student) +"~" +str(round(studentAvg,2))]
        studentAvgTotal.append((student[0],student[1],studentAvg))
    #studentAvgTotal = sorted(studentAvgTotal,key=lambda stdRoll: stdRoll.split('~')[0])
    for stdAvg in sorted(studentAvgTotal,key=lambda roll:roll[0]):
        print(f'{stdAvg[0]}~{stdAvg[1]}~{stdAvg[2]}')

StudentGrades() #calling the above function



'''
Courses
POT~Potions~1~2011-2012~Severus Snape
DADA~Defence Against the Dark ARTS~1~2011-2012~Gilderoy Lockhart
Students
RAV4309~Angelina Johnson
RAV4308~Olive Hornby
Grades
POT~1~2011-2012~RAV4309~B
POT~1~2011-2012~GRF9110~A
EndOfInput

print(inputData)

Courses
TRAN~Transfiguration~1~2011-2012~Minerva McGonagall
CHAR~Charms~1~2011-2012~Filius Flitwick
Students
SLY2301~Hannah Abbott
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2306~Malcolm Baddock
SLY2307~Marcus Belby
SLY2308~Katie Bell
SLY2309~Sirius Orion Black
Grades
TRAN~1~2011-2012~SLY2301~AB
TRAN~1~2011-2012~SLY2302~B
TRAN~1~2011-2012~SLY2303~B
TRAN~1~2011-2012~SLY2305~A
TRAN~1~2011-2012~SLY2306~BC
TRAN~1~2011-2012~SLY2308~A
TRAN~1~2011-2012~SLY2309~AB
CHAR~1~2011-2012~SLY2301~A
CHAR~1~2011-2012~SLY2302~BC
CHAR~1~2011-2012~SLY2303~B
CHAR~1~2011-2012~SLY2305~BC
CHAR~1~2011-2012~SLY2306~C
CHAR~1~2011-2012~SLY2307~B
CHAR~1~2011-2012~SLY2308~AB
EndOfInput                
'''

''' from google groups
class Course:
    def __init__(self, code, name, semester, year, instructor):
        self.code = code
        self.name = name
        self.semester = semester
        self.year = year
        self.instructor = instructor


class Student:
    def __init__(self, roll_number, full_name):
        self.roll_number = roll_number
        self.full_name = full_name
        self.grades = []

    def add_grade(self, course_code, grade):
        self.grades.append((course_code, grade))


def calculate_grade_points(grade):
    grades_to_points = {'A': 10, 'AB': 9, 'B': 8, 'BC': 7, 'C': 6, 'CD': 5, 'D': 4}
    return grades_to_points.get(grade, 0)


# Read input data and create objects
courses = {}
students = {}


current_section = None
while True:
    try:
        line = input()
    except EOFError:
        break


    if line == "EndOfInput":
        break
    elif line == "Courses":

        current_section = "Courses"
    elif line == "Students":
        current_section = "Students"
    elif line == "Grades":
        current_section = "Grades"
    else:
        if current_section == "Courses":
            course_code, course_name, semester, year, instructor = line.split("~")
            courses[course_code] = Course(course_code, course_name, semester, year, instructor)

        elif current_section == "Students":
            roll_number, full_name = line.split("~")
            students[roll_number] = Student(roll_number, full_name)

        elif current_section == "Grades":
            course_code, semester, year, roll_number, grade = line.split("~")
            students[roll_number].add_grade(course_code, grade)

# Calculate grade point averages and store results
student_results = []
for student in students.values():
    total_points = sum(calculate_grade_points(grade) for _, grade in student.grades)
    total_courses = len(student.grades)
    if total_courses > 0:
        gpa = round(total_points / total_courses, 2)
    else:
        gpa = 0
    student_results.append((student.roll_number, student.full_name, gpa))

# Print results sorted by roll number
for roll_number, full_name, gpa in sorted(student_results):
    print(f"{roll_number}~{full_name}~{gpa}")
'''



'''
Expected output -- this is part of Week 5 programming assignment. 

GRF3701~Vincent Crabbe~0\n
GRF3702~Colin Creevey~0\n
GRF3703~Dennis Creevey~0\n
GRF3704~Roger Davies~0\n
GRF3705~Cedric Diggory~0\n
GRF3706~Harold Dingle~0\n
GRF3707~Emma Dobbs~0\n
GRF3708~J. Dorny~0\n
GRF3709~B. Dunstan~0\n
GRF3710~Marietta Edgecombe~0\n
GRF3711~S. Fawcett~0\n
GRF3712~Justin Finch-Fletchley~0\n
GRF3713~Seamus Finnigan~0\n
GRF3714~Vicky Frobisher~0\n
GRF3715~Basil Fronsac~0\n
GRF3716~Anthony Goldstein~0\n
GRF3717~Gregory Goyle~5.0\n
GRF9101~Eloise Midgen~6.0\n
GRF9102~Laverne de Montmorency~6.0\n
GRF9103~Montgomery sisters~8.0\n
GRF9104~Lily Moon~9.0\n
GRF9105~Harold Potter~9.0\n
GRF9106~Theodore Nott~9.0\n
GRF9107~Garrick Ollivander~10.0\n
GRF9108~Pansy Parkinson~8.0\n
GRF9109~Padma Patil~9.0\n
GRF9110~Parvati Patil~10.0\n
HUF7201~Gwenog Jones~0\n
HUF7202~Lee Jordan~9.0\n
HUF7203~Bertha Jorkins~0\n
HUF7204~Viktor Krum~6.0\n
HUF7206~Bellatrix Lestrange~0\n
HUF7207~Neville Longbottom~4.0\n
HUF7208~Luna Lovegood~8.0\n
HUF7209~Remus John Lupin~0\n
HUF7210~Mary Macdonald~7.0\n
RAV4301~Hermione Jean Granger~7.6\n
RAV4302~Daphne Greengrass~8.0\n
RAV4303~Gellert Grindelwald~8.83\n
RAV4304~Davey Gudgeon~7.8\n
RAV4305~Rubeus Hagrid~7.2\n
RAV4306~Ciceron Harkiss~7.0\n
RAV4307~Geoffrey Hooper~8.6\n
RAV4308~Olive Hornby~7.0\n
RAV4309~Angelina Johnson~7.0\n
RAV5901~Oliver Wood~9.0\n
RAV5902~Isobel MacDougal~6.0\n
RAV5903~Morag MacDougal~0\n
RAV5904~Ernest Macmillan~0\n
RAV5905~Laura Madley~9.0\n
RAV5906~Draco Malfoy~7.0\n
RAV5907~Natalie McDonald~5.0\n
RAV5908~M. G. McGonagall~7.0\n
SLY2301~Hannah Abbott~9.0\n
SLY2302~Euan Abercrombie~7.5\n
SLY2303~Stewart Ackerley~7.75\n
SLY2304~Bertram Aubrey~7.0\n
SLY2305~Avery~8.0\n
SLY2306~Malcolm Baddock~6.75\n
SLY2307~Marcus Belby~8.25\n
SLY2308~Katie Bell~7.75\n
SLY2309~Sirius Orion Black~9.0\n
SLY2310~Melinda Bobbin~9.5\n
SLY2311~Susan Bones~7.25\n
SLY2312~Terry Boot~6.5\n
SLY2313~Eleanor Branstone~7.25\n
SLY2315~Mandy Brocklehurst~7.25\n
SLY2316~Lavender Brown~7.0\n
SLY2317~Millicent Bulstrode~6.0\n
SLY2318~S. Capper~6.5\n
SLY2319~Eddie Carmichael~6.75\n
SLY2320~Owen Cauldwell~9.0\n
SLY2321~Cho Chang~7.5\n
SLY2323~Michael Corner~7.75
'''

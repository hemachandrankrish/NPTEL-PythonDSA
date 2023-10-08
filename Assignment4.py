def mystery(l):
    if l ==[]:
        return l
    else:
        return(l[-1:]+mystery(l[:-1]))
    
#print(mystery([23,35,29,58,93,46]))
#print(list(range(6,1,-1)))
pairs = [ (x,y) for x in range(6,1,-1) for y in range(3,1,-1) if (x+y)%2 == 0 ]
#print(pairs)
# x in (6,5,4,3,2)
# y in (3,2)
# (x+y)%2==0

# 6,2
# 5,3

# 4,2
# 3,3

# 2,2

# goals = {"Country":{"Ronaldo":123,"Messi":103,"Pele":83},"Club":{"Ronaldo":[512,51,158],"Pele":[604,49,26]}}
# goals["Club"]["Messi"] = [496,71,145]
# #print(goals)

# #print(goals["Club"]["Messi"][0:] = [496,71,145])
# #print(goals["Club"]["Messi"].extend([496,71,145]))
# #print(goals["Club"]["Messi"] = [496,71,145])
# #print(goals["Club"]["Messi"] = goals["Club"]["Messi"] + [496,71,145])

# wickets = {}
# wickets[("Murali,tests")]=800
# #wickets["Murali"] = {"tests":800}
# print(wickets)

def histogram(l):
    repetition = []
    if l == []:
        return l
    else:
        for x in set(l):
            count=0
            for y in l:
                if x == y:
                    count=count+1
            repetition = repetition+[(x,count)]
    return(sorted(repetition,key=lambda item: (item[1],item[0])))


histogram([2,3,4,5,5,5,5,5,4,33,33])                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

# print(histogram([2,3,4,5,5,5,5,5,4,33,33]))

# print(histogram([13,12,11,13,14,13,7,7,13,14,12]))
# #[(11, 1), (7, 2), (12, 2), (14, 2), (13, 4)]

# print(histogram([7,12,11,13,7,11,13,14,12]))
# #[(14, 1), (7, 2), (11, 2), (12, 2), (13, 2)]

# print(histogram([13,7,12,7,11,13,14,13,7,11,13,14,12,14,14,7]))
# #[(11, 2), (12, 2), (7, 4), (13, 4), (14, 4)]

def transcript(coursedetails,studentdetails,grades):
    #coursedetails = (coursecode,coursename)
    #studentdetails = (rollnumber,name)
    #grades = (rollnumber,coursecode,grade)
    fullDetails = []
    for studenDetail in studentdetails: 
        studColl,studCourseDetails = [],[]
        for grade in grades:
            if grade[0] == studenDetail[0]:
                for courseDetail in coursedetails:
                    if grade[1] == courseDetail[0]:
                        studCourseDetails = sorted(studCourseDetails+[(courseDetail[0],courseDetail[1],grade[2])])
        studColl = (studColl+[studenDetail[0],studenDetail[1]])
        fullDetails = sorted(fullDetails+[(tuple((studColl+[studCourseDetails])))])
        #print(fullDetails)
    return fullDetails

#print(transcript([("MA101","Calculus"),("PH101","Mechanics"),("HU101","English")],[("UGM2021001","Rohit Grewal"),("UGP2021132","Neha Talwar")],[("UGM2021001","MA101","AB"),("UGP2021132","PH101","B"),("UGM2021001","PH101","B")]))
#print(transcript([("T4","Test 1"),("T2","Test 2"),("T3","Test 3")],[("Captain","Rohit Sharma"),("Batsman","Virat Kohli"),("No3","Cheteshwar Pujara")],[("Batsman","T1","14"),("Captain","T4","33"),("No3","T4","30"),("Batsman","T2","55") ,("Captain","T2","158"),("No3","T2","19"), ("Batsman","T3","33"),("Captain","T3","95"),("No3","T3","51")]))
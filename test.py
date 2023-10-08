set1 = {1,2,3,4}
print(set1)

#print(2**2**1%5)
print(4%5)
a= [0,4,2,3]
for a[-3] in a:
    print(a[-3],end =" ")

dict1 = {'apple':'cat a','ball':'cat b','apple':'cat c'}
print(dict1['apple'])

hundreds = {}
hundreds["Tendulkar, international"] = 100
print("1",hundreds)
hundreds["Tendulkar"] = {"international":100}
print("2",hundreds)
hundreds[("Tendulkar","international")] = 100
print("3",hundreds)
#hundreds[["Tendulkar","international"]] = 100

wickets = {"Tests":{"Ishant":[3,5,2,3],"Shami":[4,4,1,0],"Bumrah":[2,1,7,4]},"ODI":{"Ishant":[2,0],"Shami":[1,2]}} 

#wickets["ODI"]["Bumrah"][0:] = [4,4]
#print(wickets)
#wickets["ODI"]["Bumrah"].extend([4,4])
#print(wickets)
wickets["ODI"]["Bumrah"] = [4,4]
print(wickets)
#wickets["ODI"]["Bumrah"] = wickets["ODI"]["Bumrah"] + [4,4]
#print(wickets)

x = ["slithy",[7,10,12],2,"tove",1]  # Statement 1 
y = x[0:50] 
print(y)
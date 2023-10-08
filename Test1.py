testList = ['SLY2301~Hannah Abbott~9.5',
'SLY2312~Euan Abercrombie~0',
'SLY2303~Stewart Ackerley~8.0',
'SLY2304~Bertram Aubrey~0',
'SLY2305~Avery~8.5',
'SLY2306~Malcolm Baddock~6.5',
'SLY2307~Marcus Belby~8.0',
'SLY2308~Katie Bell~9.5',
'SLY2309~Sirius Orion Black~9.0']

testList = sorted(testList, key= lambda roll:roll.split('~')[0])

#print(testList)

# x = [1,2,3,4]
# print(x)
# x.insert(0,0)
# print(x)
# x.pop()
# print(x)


a = set([1,3,5,7,9])
b = set([2,4,6,8])

print(a|b)
print(a&b)
print(a-b)
print(a^b)  
u = set([1,3,5])
v = set([2,4,6])
print(u == v^(u | v))
print(u == (v^u))
print( u == v | (u^v))
print( u == u^(v | u))
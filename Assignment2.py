# def updateList(L,i,v):
#     if i >=0 and i<len(L):
#         L[i] = v
#         return(True)
#     else:
#         v= v+1
#         return(False)
    
# ns = [13,14,15]
# z = 8
# #updateList(ns,4,z)
# #print(ns)
# #print(z)



# x = ["slithy",[7,10,12],2,"tove",1]  # Statement 1
# y = x[0:50]                          # Statement 2
# z = y                                # Statement 3
# w = x                                # Statement 4
# x[0] = x[0][:5] + 'ery'              # Statement 5
# y[2] = 4                             # Statement 6
# z[4] = 42                            # Statement 7
# #w[0][:3] = 'fea'                     # Statement 8
# x[1][0] = 5555                       # Statement 9
# #a = (x[4][1] == 1)                   # Statement 10

# b = [23,44,87,100]
# a = b[1:]
# d = b[2:]
# c = b
# d[0] = 97
# c[2] = 77
# print(a,b,c,d)

# def mystery(l):
#   l = l[1:]
#   return()

# mylist = [7,11,13]
# mystery(mylist)
# print(mylist)


def primeproduct(m):
    
    if m<0:
        return False
    
    print("first find the list of numbers/factors")

    l3 = []
    for i in range(2,(m//2)+1):
        if(m%i ==0):
            l3 = l3 + [i]
    x = 0

    if l3 == [1]:
        return True
    else:
        for j in l3:
            for k in l3:
             if(j*k == m and isPrime(j) and isPrime(k)):
               x = x+1
    if x >= 1:
        return True
    else:
        return False

def isPrime(s):
    if s < 1:
        return False
    key = 0
    if s == 1 or s==2:
        return True
    else:
        for i in range(2,s+1):
            if(s%i == 0):
                key = key +1
    if key > 1:
        return False
    else:
        return True
  
    

#print(isPrime(11))
#print(primeproduct(63))
# print(primeproduct(4))
# print(primeproduct(5))
# print(primeproduct(3))

             
def delchar(s,c):
    if len(c)!=1:
        return s
    else:
        m = ""
        for char in s:
            if (char != c):
                m = m + char
        return m
    
# print(delchar("banana","a"))
    
def shuffle(l1,l2):
    if len(l1)>=0 and len(l2)>=0:
        l4 = []
        i, j = 0,0

        while i < len(l1) or j < len (l2):
            if i < len(l1):
                l4 = l4 + [l1[i]]
                i = i+1
            if j < len(l2):
                l4 = l4 + [l2[j]]
                j = j+1
        return l4
    else:
        return []
    
print(shuffle([],[2,4,8,6,8,9]))
print(shuffle([3,5],[]))
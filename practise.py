strings = ['cloud','ith','hit','could','hello','world','they see','the eyes']

def strAnagram(ls):
    
    anag_dict = {}

    for s in ls:
        _sorted = ''.join(sorted(s))
        if _sorted in anag_dict:
            anag_dict[_sorted].append(s)
        else:
            anag_dict[_sorted] = [s]
        analogstr = [group for group in anag_dict.values() if len(group) >1]

        flatstr = [s for group in analogstr for s in group]
        #print(flatstr)
    return flatstr
    



#dchbaeglkonmji
#eibigfcadh
#dgbejiklfcah
#mioprtanlik

def true():
    return True

def error():
    return 1/0




if __name__ == "__main__":
   #print(strAnagram(strings))
   #print(all(f() for f in [true, error]))
    # print(all([f() for f in [true, error]]))
    nums = {1,2,2,3}
    print(len(nums))

    #print (285// 10)

    def mystery(l):
        print(id(l))
        # l = l+[5]
        # print(id(l))
        l.extend([12])
        print(id(l))
        print("sec",l)
        return()
    mylist = [22,34,57]
    #mystery(mylist)
    #print(mylist)
    #print(id(mylist))

    def g(n):
        s=0
        for i in range(1,n+1):
            if n%i == 0:
                s = s+1
        return(s)
    print(g(23))


    def f(m):
        if m == 0:
            return(0)
        else:
            return(m+f(m-1))
    print(f(5))
 

    def f():
        global x1, l1
        x1 = x1 + [5]
        x1.extend([10])
        l1 = l1+ 10
        x3=x1+[11]
        x2=x1+[4]


    
    x1,x2,x3= [5],[6],[7]
    l1,l2,l3 = 3,4,8
    f()
    print(x1,x2,x3,l1,l2,l3)

my_dict = {1:"Charles",2:"Babbage"}
print(*my_dict)
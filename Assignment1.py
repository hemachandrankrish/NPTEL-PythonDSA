def g(y):
    b = 0
    while y >= 3:
        (y,b) = (y/3,b+1)
    #return(b)
    print ('value is ', b)
g(728)

def f(n):
    s = 0
    for i in range(2,n):
        if n%i == 0 and i%2 == 1:
            s = s+1
    return(s)

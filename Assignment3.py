def expanding(l):
    if l == []:
        return False
    elif len(l)<=2:
        return False
    else:
        return diff(l)
    
def diff(l):
    m = []
    for pos in range(1,len(l)): ## l=[2,3,5] 
        posA = l[pos]
        posB = l[pos-1]
        if posA < posB:
            posA, posB = posB,posA
        m = m + [posA-posB]
    for val in range(0,len(m)-1):
        while val < len(m)-1:
            if m[val] < m[val +1]:
                flag = True
            else:
                flag = False
            val = val+1
    return flag  


print(expanding([1,3,7,2,9]))
print(expanding([1,3,7,2,-3]))
print(expanding([1,3,7,10]))
print(expanding([-2,-3,5,-7]))


def sumsquare(l):
    iOdd, iEven = 0,0
    for val in l:
        if val%2 == 0:
            iEven = iEven + val*val
        else:
            iOdd = iOdd + val*val
    return[iOdd,iEven]

# print(sumsquare([-4]))
# print(sumsquare([2,4,6]))
# print(sumsquare([-1,-2,3,7]))


def transpose(a):
    b=a.copy()
    if len(b)==0:
        return b
    else:
        return transp(b)

def transp(b):
    lenA = len(b)
    lenB = len(b[0])
    l= []
    for i in range(0,lenB):
        k = []
        for j in range(0,lenA):
            k = k + [b[j][i]]
        l = l + [k]
    return l


# print(transpose([[1,-2,3],[4,-5,6],[0,1,0],[-1,0,1]]))
# print(transpose([[1, 2, 3, 4], [5, 6, 7, 8]]))
# print(transpose([[-5 ,5]]))

# print(transpose([[1,2,3],[4,5,6]]))
# print(transpose([[1],[2],[3]]))
# print(transpose([[3]]))
# print(transpose([[3]]))

#print([[1,2,3] + [4,5,6]])

def transpose_matrix(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        transposed_row = [row[i] for row in matrix]
        transposed.append(transposed_row)
    return transposed

# Original matrix
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8]]

# Display original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Compute and display the transpose
transposed_matrix = transpose_matrix(matrix)
print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)

    
print([range(4)])
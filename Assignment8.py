def getData():
    inputData = []
    while(True):
        try:
            count = int(input())

            if count <= 0 or count > 2500:
                break
            else:
                for i in range(0,count):
                    inData = int(input())
                    inputData.append(inData)
                break
        except ValueError:
            #print("error in inputs")
            break
        except EOFError:
            break
    return inputData

#print(getData())


def getMaxDivSequence():
    inputDataMain = getData()
    #inputDataMain = [2,3,-5,6,-9,-12]
    #inputDataMain = [2,4,8,16,7]
    #inputDataMain = [2,11,16,12,36,60,71,17,29,144,288,129,432,993]
    #inputDataMain = [2,3 ,7 ,8 ,14 ,39 ,145 ,76 ,320]
    #inputDataMain = [14,2,11,16, 12, 36,60, 71,17, 29,144,288,129,432,993]
    maxCount = 1
    storedMax = {}
    for i in range(len(inputDataMain)):
        if i == 0:
            storedMax[inputDataMain[i]] = 1
        else:
            storedMax[inputDataMain[i]] = 0
    lenInput = len(inputDataMain)
    if lenInput == 0:
        return 0
    else:
        for i in (range(0,lenInput)):
            maxSequence = 1
            iNum = inputDataMain[i]
            for j in (range(0,i)):
                if iNum!=0 and inputDataMain[j]!=0 and iNum % inputDataMain[j] == 0:
                    maxSequence = max(maxSequence,storedMax[inputDataMain[j]]+1) 
            storedMax[inputDataMain[i]]= maxSequence
    return max(storedMax.values())

print(getMaxDivSequence())


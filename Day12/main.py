
startCoord = []
endCoord = []

def main():
    stringInput = readFile("input1.txt")
    print(stringInput[0])


    arrayInput = getArrayInput(stringInput)
    arrayInput[startCoord[0]][startCoord[1]] = 0
    arrayInput[endCoord[0]][endCoord[1]] = 26


    for i in arrayInput:
        for x in i:
            print("%3d" %(x), end= "")
        print("")
    print()
    print(startCoord)
    print(endCoord)




def getArrayInput(stringInput):
    global startCoord
    global endCoord

    lineCounter = 0
    treeArray = []

    for line in stringInput:
        listLine = list(line)
        lineArray = []
        charCounter = 0
        for i in listLine:
            if i.__contains__("\n"):
                pass
            else:
                lineArray.append(ord(i)-97)

            #Get start and end coordinates
            if i.__contains__("S"):
                startCoord = [lineCounter, charCounter]

            if i.__contains__("E"):
                endCoord = [lineCounter, charCounter]

            charCounter += 1
        treeArray.append(lineArray)
        lineCounter += 1
    return treeArray


def readFile(inputFileName):
    file = open(inputFileName, 'r')
    lines = file.readlines()
    return lines

if __name__ == '__main__':
    main()



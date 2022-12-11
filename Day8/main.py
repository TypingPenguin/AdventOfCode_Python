

def part1():
    visibleTreeCounter = 0
    stringInput = readFile("input1.txt")

    treeArray = getTreeArray(stringInput)

    rows = (len(treeArray))
    columns = len(treeArray[0])

    print(rows, columns)

    for row in range (0,rows):
        for column in range (0, columns):

            stopLooking = 0

            lookUp = 1
            lookUpCounter = row
            lookDown = 1
            lookDownCounter = row
            lookLeft = 1
            lookLeftCounter = column
            lookRight = 1
            lookRightCounter = column

            #Look Up
            if stopLooking == 0:
                for looker in range (row-1, -1,-1):
                    if treeArray[looker][column] >= treeArray[row][column]:
                        lookUp = 0
                        break
                if lookUp == 1:
                    stopLooking = 1


            #Look Down
            if stopLooking == 0:
                for looker in range (row+1, rows, 1):
                    if treeArray[looker][column] >= treeArray[row][column]:
                        lookDown = 0
                        break
                if lookDown == 1:
                    stopLooking = 1

            #Look Left
            if stopLooking == 0:
                for looker in range (column-1, -1,-1):
                    if treeArray[row][looker] >= treeArray[row][column]:
                        lookLeft = 0
                        break
                if lookLeft == 1:
                    stopLooking = 1


            #Look Right
            if stopLooking == 0:
                for looker in range (column+1, columns,):
                    if treeArray[row][looker] >= treeArray[row][column]:
                        lookRight = 0
                        break
                if lookRight == 1:
                    stopLooking = 1



            if stopLooking == 1:
                visibleTreeCounter +=1

            print(visibleTreeCounter)

def part2():
    sum = 0
    stringInput = readFile("input1.txt")

    treeArray = getTreeArray(stringInput)

    rows = (len(treeArray))
    columns = len(treeArray[0])

    print(rows, columns)

    for row in range (0,rows):
        for column in range (0, columns):

            stopLooking = 0

            lookUp = 1
            lookUpCounter = 0
            lookDown = 1
            lookDownCounter = 0
            lookLeft = 1
            lookLeftCounter = 0
            lookRight = 1
            lookRightCounter = 0

            #Look Up
            for looker in range (row-1, -1,-1):
                lookUpCounter += 1
                if treeArray[looker][column] >= treeArray[row][column]:
                    lookUp = 0
                    break
            if lookUp == 1:
                stopLooking = 1


            #Look Down
            for looker in range (row+1, rows, 1):
                lookDownCounter += 1
                if treeArray[looker][column] >= treeArray[row][column]:
                    lookDown = 0
                    break

            if lookDown == 1:
                stopLooking = 1

            #Look Left
            for looker in range (column-1, -1,-1):
                lookLeftCounter += 1
                if treeArray[row][looker] >= treeArray[row][column]:
                    lookLeft = 0
                    break
            if lookLeft == 1:
                stopLooking = 1


            #Look Right
            for looker in range (column+1, columns,):
                lookRightCounter += 1
                if treeArray[row][looker] >= treeArray[row][column]:
                    lookRight = 0
                    break
            if lookRight == 1:
                stopLooking = 1


            intermediateSum = lookRightCounter * lookLeftCounter * lookUpCounter * lookDownCounter


            if row == 1 and column == 2:
                print(lookRightCounter, lookLeftCounter, lookUpCounter, lookDownCounter)
            print(intermediateSum)
            if intermediateSum > sum:
                sum = intermediateSum
            print(sum)


def getTreeArray(stringInput):
    lineCounter = 0
    treeArray = []
    for line in stringInput:
        listLine = list(line)
        lineArray = []
        for i in listLine:
            if i.__contains__("\n"):
                pass
            else:
                lineArray.append(int(i))
        treeArray.append(lineArray)
        lineCounter += 1
    return treeArray


def readFile(inputFileName):
    file = open(inputFileName, 'r')
    lines = file.readlines()
    return lines

if __name__ == '__main__':
    part1()
    part2()



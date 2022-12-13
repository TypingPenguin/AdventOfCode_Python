import queue
import os
#import pyautogui


startCoord = []
endCoord = []
cost = [[]]
arrayInput =[[]]

maxX = 0
maxY = 0
queue = queue.Queue()

def main():
    global arrayInput
    global cost


    stringInput = readFile("input1.txt")
    print(stringInput[0])


    arrayInput = getArrayInput(stringInput)
    arrayInput[startCoord[0]][startCoord[1]] = 0
    arrayInput[endCoord[0]][endCoord[1]] = 25

    maxX = len(arrayInput[0])
    maxY = len(arrayInput)
    print(maxX,maxY)
    cost = [["."]* maxX for i in range(maxY)]



    toStringArray(arrayInput)
    print(startCoord)
    print(endCoord)

    toStringArray(cost)


    #take start coordinate
    currentX = startCoord[1]
    currentY = startCoord[0]

    cost[currentY][currentX] = 0

    #set first coord in queue
    queue.put([currentX,currentY])
    print(currentX,currentY)

    counter = 0
    while (True):

        currentCoord = queue.get()
        currentX = currentCoord[0]
        currentY = currentCoord[1]


        #down
        if currentY+1 < maxY:
            nextCoord(currentX, currentY, 0, 1)
            print("DOWN")
        #right
        if currentX+1 < maxX:
            nextCoord(currentX, currentY, 1, 0)
            print("RIGHT")
        #up
        if currentY-1 >= 0:
            nextCoord(currentX, currentY, 0, -1)
            print("UP")
        #left
        if currentX-1 >= 0:
            nextCoord(currentX, currentY, -1, 0)
            print("LEFT")


        if queue.empty():
            print( "Queue empty!")
            break;


        counter +=1



    print(toStringArray(cost))
        #pyautogui.hotkey('command', 'l')
    print(toStringArray(arrayInput))
    #print (cost[currentX][currentY])



    print(cost[endCoord[0]][endCoord[1]])
    #if they have as value in cost[] == "." do current cost +1
    #add to queue.
    #take first of queue etc until empty.



#sets cost of Coord and puts it in the queue
def nextCoord(currentX, currentY, xAddition, yAddition):
    currentValue = arrayInput[currentY][currentX]
    nextValue = arrayInput[currentY + yAddition][currentX + xAddition]
    if nextValue - currentValue <= 1:
        if cost[currentY + yAddition][currentX + xAddition] == ".":
            cost[currentY + yAddition][currentX + xAddition] = cost[currentY][currentX] + 1
            print(queue.qsize())
            queue.put([currentX+xAddition,currentY+yAddition])
            print(queue.qsize())



def toStringArray(arrayInput):
    for i in arrayInput:
        for x in i:
            print("%4s" % (x), end="")
        print("")
    print()


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



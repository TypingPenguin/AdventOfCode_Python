
size = 50
width = size
height = size
headRow = int(size/2)
headColumn = int(size/2)
tailRow = int(size/2)
tailColumn = int(size/2)
startRow = int(size/2)
startColumn = int(size/2)


tailLength = 9
tailArray = [[int(size/2),int(size/2)] * 1 for i in range(tailLength)]

tailSet = {}
tailSet = set()

grid = [["."]* width for i in range(height)]
grid[startRow][startColumn] = "s"



def main():

    toString()

    stringInput = readFile("input.txt")
    for line in stringInput:
        line = line.replace("\n","")
        line = line.split(" ")

        if line[0] == "R":
            for i in range(0,int(line[1])):
                moveHead(1, 0)

                for x in range(len(tailArray)):
                    print(x)
                    doTail(x)
                registerTail(tailLength-1)

        elif line[0] == "L":
            for i in range(0,int(line[1])):
                moveHead(-1, 0)
                for x in range(len(tailArray)):
                    doTail(x)
                registerTail(tailLength-1)


        elif line[0] == "U":
            for i in range(0,int(line[1])):
                moveHead(0, -1)
                for x in range(len(tailArray)):
                    doTail(x)
                registerTail(tailLength-1)

        elif line[0] == "D":
            for i in range(0,int(line[1])):
                moveHead(0, 1)
                for x in range(len(tailArray)):
                    doTail(x)
                registerTail(tailLength-1)




    print("--------------------------------")
    toString()
    print(tailArray)
        #print(headRow, headColumn)
        #print(tailRow,tailColumn)
    print(tailSet)
    print(len(tailSet))


def registerTail(counter):
    tailSet.add(str(tailArray[counter][0]) + " " + str(tailArray[counter][1]))
    #tailSet.add([tailRow,tailColumn])


def doTail(counter):
    if counter == 0:
        if not headClose():
            if ((headColumn-tailArray[counter][1])/2) > 0.0:
                horizontal = int(((headColumn-tailArray[counter][1])/2)+0.5)
            elif ((headColumn-tailArray[counter][1])/2) < 0.0:
                horizontal = int(((headColumn-tailArray[counter][1])/2)-0.5)
            else:
                horizontal = int(((headColumn-tailArray[counter][1])/2))

            if ((headRow-tailArray[counter][0])/2) > 0.0:
                vertical = int(((headRow-tailArray[counter][0])/2)+0.5)
            elif ((headRow-tailArray[counter][0])/2) < 0.0:
                vertical = int(((headRow-tailArray[counter][0])/2)-0.5)
            else:
                vertical = int(((headRow-tailArray[counter][0])/2)-0.5)

            moveTail(horizontal,vertical, counter)
    else:
        if not tailClose(counter):
            if ((tailArray[counter-1][1]-tailArray[counter][1])/2) > 0.0:
                horizontal = int(((tailArray[counter-1][1]-tailArray[counter][1])/2)+0.5)
            elif ((tailArray[counter-1][1]-tailArray[counter][1])/2) < 0.0:
                horizontal = int(((tailArray[counter-1][1]-tailArray[counter][1])/2)-0.5)
            else:
                horizontal = int(((tailArray[counter-1][1]-tailArray[counter][1])/2))

            if ((tailArray[counter-1][0]-tailArray[counter][0])/2) > 0.0:
                vertical = int(((tailArray[counter-1][0]-tailArray[counter][0])/2)+0.5)
            elif ((tailArray[counter-1][0]-tailArray[counter][0])/2) < 0.0:
                vertical = int(((tailArray[counter-1][0]-tailArray[counter][0])/2)-0.5)
            else:
                vertical = int(((tailArray[counter-1][0]-tailArray[counter][0])/2)-0.5)

            moveTail(horizontal,vertical, counter)
def tailClose(counter):
    return abs(tailArray[counter][0]-tailArray[counter-1][0]) < 2 and abs(tailArray[counter][1] - tailArray[counter-1][1]) < 2
def headClose():
    return abs(tailArray[0][0]-headRow) < 2 and abs(tailArray[0][1] - headColumn) < 2

def moveTail(horizontal, vertical, counter):
    global tailRow
    global tailArray
    if counter == 0:
        print (horizontal,vertical)
    tailArray[counter][1] += horizontal
    tailArray[counter][0] += vertical
def moveHead(horizontal, vertical):
    global headRow
    global headColumn
    headColumn += horizontal
    headRow += vertical

def toString():
    global grid

    grid = [["."]* width for i in range(height)]

    for x in tailSet:
        x = x.split(" ")
        grid[int(x[0])][int(x[1])] = "#"

    for x in range(tailLength,0,-1):
        print (x)
        grid[tailArray[x-1][0]][tailArray[x-1][1]] = str(x)

    grid[startRow][startColumn] = "s"
    grid[tailArray[tailLength-1][0]][tailArray[tailLength-1][1]] = "T"
    print(headRow,headColumn)
    grid[headRow][headColumn] = "H"



    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            print (grid[x][y], end='')
        print('')

def readFile(inputFileName):
    file = open(inputFileName, 'r')
    lines = file.readlines()
    return lines

if __name__ == '__main__':
    main()



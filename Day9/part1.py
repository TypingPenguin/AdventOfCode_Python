
size = 50
width = size
height = size
headRow = int(size/2)
headColumn = int(size/2)
tailRow = int(size/2)
tailColumn = int(size/2)
startRow = int(size/2)
startColumn = int(size/2)

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
                doTail()
                registerTail()

        elif line[0] == "L":
            for i in range(0,int(line[1])):
                moveHead(-1, 0)
                doTail()
                registerTail()


        elif line[0] == "U":
            for i in range(0,int(line[1])):
                moveHead(0, -1)
                doTail()
                registerTail()

        elif line[0] == "D":
            for i in range(0,int(line[1])):
                moveHead(0, 1)
                doTail()
                registerTail()




    print("--------------------------------")
    toString()
        #print(headRow, headColumn)
        #print(tailRow,tailColumn)
    print(tailSet)
    print(len(tailSet))


def registerTail():
    tailSet.add(str(tailRow) + " " + str(tailColumn))
    #tailSet.add([tailRow,tailColumn])


def doTail():
    if not headClose():

        if ((headColumn-tailColumn)/2) > 0.0:
            horizontal = int(((headColumn-tailColumn)/2)+0.5)
        elif ((headColumn-tailColumn)/2) < 0.0:
            horizontal = int(((headColumn-tailColumn)/2)-0.5)
        else:
            horizontal = int(((headColumn-tailColumn)/2))

        if ((headRow-tailRow)/2) > 0.0:
            vertical = int(((headRow-tailRow)/2)+0.5)
        elif ((headRow-tailRow)/2) < 0.0:
            vertical = int(((headRow-tailRow)/2)-0.5)
        else:
            vertical = int(((headRow-tailRow)/2)-0.5)


        #print("moving tail")
        #print(horizontal, vertical)
        #if headColumn == tailColumn:
            #moveTail((headRow-tailRow)/2)
        #elif headRow == tailRow:
            #moveTail((headColumn-tailColumn)/2)
        #else:
        moveTail(horizontal,vertical)

def headClose():
    return abs(tailRow-headRow) < 2 and abs(tailColumn - headColumn) < 2

def moveTail(horizontal, vertical):
    global tailRow
    global tailColumn
    tailColumn += horizontal
    tailRow += vertical
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


    grid[startRow][startColumn] = "s"
    grid[tailRow][tailColumn] = "T"
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



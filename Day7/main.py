fileSizeDict = {}
pathDict = {}
maxSize = 100000
totalSpace = 70000000
neededFreeSpace = 30000000



#TODO clean up code one day
def main():
    stringInput = readFile("input2.txt")
    currentPath = ""
    for line in stringInput:
        if (line.__contains__("$")):
            counter = 0
            if line.__contains__("cd .."):
                while 1:
                    c = currentPath[-1]

                    if c == "/" and counter == 1:
                        break
                    elif c == "/":
                        counter = 1
                    currentPath = currentPath[:-1]
                #print(currentPath)
                do_something()
            elif (line.__contains__("cd /")):
                currentPath += "/"
            elif (line.__contains__("cd")):
                newPath = line.split(" ")
                print(line)
                addedPath = newPath[2].replace("\n", "")
                currentPath += addedPath + "/"
                #print(currentPath)

            elif (line.__contains__("dir")):
                do_something()

            elif (line.__contains__("ls")):
                do_something()

            else:
                line = line.split()
                fileSizeDict.update({line[1]: line[0]})

        #add path to Dictionary
        if pathDict.get(currentPath) == None:
            pathDict.update({currentPath: 0})
    print(pathDict.keys())


    currentPath = ""
    print(stringInput)
    for line in stringInput:
        print("This is the current line being processed:" + line)
        #Same code as above to make path
        counter = 0
        if (line.__contains__("$")):
            if line.__contains__("cd .."):
                print(line.__contains__("h.lst"))
                while 1:
                    c = currentPath[-1]

                    if c == "/" and counter == 1:
                        break
                    elif c == "/":
                        counter = 1
                    currentPath = currentPath[:-1]
                #print(currentPath)
                do_something()
            elif (line.__contains__("cd /")):
                print(line.__contains__("h.lst"))
                currentPath += "/"
            elif (line.__contains__("cd")):
                print(line.__contains__("h.lst"))

                newPath = line.split(" ")
                addedPath = newPath[2].replace("\n", "")
                currentPath += addedPath + "/"
                #print(currentPath)

            elif (line.__contains__("dir")):
                do_something()

            elif (line.__contains__("ls")):
                do_something()

        elif not line.__contains__("dir"):
            print(line)
            line = line.split()
            parentPath = currentPath
            print("NEW PARENT PATH PROCEDURE ======================")
            print(int(line[0]))
            #print(parentPath)
            while len(parentPath) > 0:
                print(parentPath)
                pathDict.update({parentPath: (pathDict.get(parentPath) + int(line[0]))})
                counter = 0
                if len(parentPath) > 1:
                    while 1:
                        c = parentPath[-1]
                        if c == "/" and counter == 1:
                            break
                        elif c == "/":
                            counter = 1
                        parentPath = parentPath[:-1]
                else:
                    break;




    sum = 0
    for key in pathDict.keys():
        if pathDict.get(key) <= maxSize:
            sum += pathDict.get(key)
    print("SUM FOR PART1:")
    print(sum)


    pathToDelete = ""
    sizeCurrentFolder = 999999999
    spaceToDelete = neededFreeSpace - (totalSpace - pathDict.get("/"))
    for key in pathDict.keys():
        if pathDict.get(key) > spaceToDelete and pathDict.get(key) < sizeCurrentFolder:
            pathToDelete = key
            sizeCurrentFolder = pathDict.get(key)

    print("Size for PART2:")
    print(pathToDelete)
    print(sizeCurrentFolder)



def do_something():
    pass


def readFile(inputFileName):
    file = open(inputFileName, 'r')
    lines = file.readlines()
    return lines


if __name__ == '__main__':
    main()

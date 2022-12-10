fileSizeDict = {}

dict = {Name: "Parent",
        child:{
            name
        }
        }
def main():
    stringInput = readFile("input1.txt")
    for line in stringInput:
        if (line.__contains__("cd..")):
            do_something()
        elif (line.__contains__("cd /")):
            do_something()
        elif (line.__contains__("cd")):
            do_something()
        elif (line.__contains__("dir")):
            do_something()
        elif (line.__contains__("ls")):
            do_something()
        else:
            line = line.split()
            fileSizeDict.update({line[1]:line[0]})

fileSizeDict.update({"something":"sasfdasd"})
fileSizeDict.update({"something":"sasfddasd"})

print(fileSizeDict.get("something"))

def do_something():
    pass
def readFile(inputFileName):
    file = open(inputFileName, 'r')
    lines = file.readlines()
    return lines

if __name__ == '__main__':
    main()

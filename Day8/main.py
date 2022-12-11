
def main():
    stringInput = readFile("input.txt")
    for line in stringInput:
        print(line.split(""))


def readFile(inputFileName):
    file = open(inputFileName, 'r')
    lines = file.readlines()
    return lines

if __name__ == '__main__':
    main()



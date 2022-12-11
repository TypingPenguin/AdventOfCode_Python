
def main():
    stringInput = readFile("input.txt")



def readFile(inputFileName):
    file = open(inputFileName, 'r')
    lines = file.readlines()
    return lines

if __name__ == '__main__':
    main()



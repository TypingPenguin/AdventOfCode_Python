from collections import Counter
# Change stringInput with appropriate string

def main():
    stringInput = readFile("input.txt")
    #Part1 of AdventOfCode
    markFinder(stringInput[0], 4)
    #Part2 of AdventOfCode
    markFinder(stringInput[0], 14)

def readFile(inputFileName):
    file = open(inputFileName, 'r')
    lines = file.readlines()
    return lines

def do_find_duplicates(x):
    for key,val in Counter(x).items():
        if val > 1:
            return 0;
    return 1;


def markFinder(stringInput, lengthMarker):
    compareString = ""
    for i in range(lengthMarker,len(stringInput)):
        compareString = stringInput[i-lengthMarker:i]
        if do_find_duplicates(compareString):
            print(i)
            break

if __name__ == '__main__':
    main()

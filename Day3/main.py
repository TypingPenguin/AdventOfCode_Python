def main():
    day3()
    day3_2()


def day3():
    # Using readlines()
    file1 = open('input2.txt', 'r')
    Lines = file1.readlines()

    sum = 0
    for line in Lines:
        #print("{}".format(line.strip()))
        line = line.strip()
        middle = int((len(line)/2))
        middle2 = middle+1
        firsthalf = slice(0,middle)
        secondhalf = slice(middle, len(line))
        #print(firsthalf)
        #print(secondhalf)
        string1 = line[firsthalf]
        string2 = line[secondhalf]
        #print(line[firsthalf])
        #print(line[secondhalf])
        checkstring = ""
        for char in string2:
            if string1.__contains__(char):
                if not checkstring.__contains__(char):
                    checkstring += char
                    #print(ord("A"))
                    #print(char, ord(char))
                    if ord(char) > 96:
                        sum += ord(char) - 96
                    else:
                        sum+= ord(char) - 38
        #print("this is the sum:",sum)
    print("Sum part 1: ",sum)

def day3_2():

    AMOUNT_OF_LINES = 3
    # Using readlines()
    file1 = open('input2.txt', 'r')
    Lines = file1.readlines()

    sum = 0
    counter = 0
    stringCompare = ""
    intermediateStringCompare = ""
    for line in Lines:

        if counter < AMOUNT_OF_LINES:
            if counter == 0:
                stringCompare = line
                counter += 1
            elif counter == 1 :
                intermediateStringCompare = ""
                for char in stringCompare:
                    if line.__contains__(char):
                        intermediateStringCompare += char
                counter += 1
            elif counter == 2 :
                for char in intermediateStringCompare:
                    if line.__contains__(char):
                        if ord(char) > 96:
                            sum += ord(char) - 96
                        else:
                            sum+= ord(char) - 38
                        break
                counter = 0
    print("Sum part 2: ", sum)

#=================================================

if __name__ == '__main__':
    main()

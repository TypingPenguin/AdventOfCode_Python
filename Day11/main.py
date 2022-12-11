

maxMonkeys = 0
maxRounds = 10000
currentMonkey = 0
moduloOfDivisible = 9699690

monkeyInspectedDictionary = {}


def main():
    global maxMonkeys
    global currentMonkey


    stringInput = readFile("input1.txt")

    #Get amount of monkeys
    for line in stringInput:
        if line.__contains__("Monkey"):
            line = line.replace(":\n","")
            line = line.split(" ")
            maxMonkeys = int(line[1])
            monkeyInspectedDictionary.update({maxMonkeys:0})

    print(maxMonkeys)
    print(monkeyInspectedDictionary)
    monkeyArray = [[] * 1 for i in range(maxMonkeys+1)]
    print(monkeyArray)



    for round in range(1, maxRounds+1):
        #Round1
        lineCounter = -1
        for line in stringInput:
            lineCounter += 1
            if line.__contains__("Monkey"):
                line = line.replace(":\n","")
                line = line.split(" ")
                currentMonkey = int(line[1])
            elif line.__contains__("Starting items:"):
                line = line.replace(",","")
                line = line.replace("\n","")
                line = line.replace("  Starting items: ","")
                line = line.split(" ")


                if round == 1:
                    for x in line:
                        monkeyArray[currentMonkey].append(int(x))

                #update items he has inspected
                monkeyInspectedDictionary.update({int(currentMonkey): monkeyInspectedDictionary.get(int(currentMonkey)) + len(monkeyArray[currentMonkey])})


            elif line.__contains__("Operation:"):
                line = line.replace("  Operation: new = ","")
                line = line.replace("\n","")
                line = line.split(" ")


                #Multiply to new value
                #print(line)
                for x in range(len(monkeyArray[currentMonkey])):
                    if line[0] == "old":
                        operator1 = monkeyArray[currentMonkey][x]
                    else:
                        operator1 = int(line[0])

                    if line[2] == "old":
                        operator2 = monkeyArray[currentMonkey][x]
                    else:
                        operator2 = int(line[2])


                    if line[1] == "+":
                        monkeyArray[currentMonkey][x] = operator1 + operator2
                    elif line[1] == "*":
                        monkeyArray[currentMonkey][x] = operator1 * operator2


                for x in range(len(monkeyArray[currentMonkey])):
                    monkeyArray[currentMonkey][x] = int(monkeyArray[currentMonkey][x] % moduloOfDivisible)



                #print(monkeyArray)

            elif line.__contains__("Test:"):
                line = line.replace("  Test: divisible by ","")
                line = line.replace("\n","")
                line = line.split(" ")

                removeElements = []
                for x in range(len(monkeyArray[currentMonkey])):

                    #If divisible
                    if monkeyArray[currentMonkey][x] % int(line[0]) == 0:
                        throwMonkey = stringInput[lineCounter+1]
                        #print(throwMonkey)
                        throwMonkey.replace("\n","")
                        throwMonkey = throwMonkey.replace("    If true: throw to monkey ", "")
                        throwMonkey = throwMonkey.split(" ")
                        #print(throwMonkey)


                    else:
                        throwMonkey = stringInput[lineCounter+2]
                        #print(throwMonkey)
                        throwMonkey = throwMonkey.replace("\n","")
                        throwMonkey = throwMonkey.replace("    If false: throw to monkey ", "")
                        throwMonkey = throwMonkey.split(" ")



                    #print("DEBUG:" , int(throwMonkey[0]))
                    monkeyArray[int(throwMonkey[0])].append(monkeyArray[currentMonkey][x])
                    removeElements.append(monkeyArray[currentMonkey][x])

                for x in removeElements:
                    monkeyArray[currentMonkey].remove(x)


        if round % 1000 == 0:
            #print(monkeyArray)
            print(monkeyInspectedDictionary)
            print("END OF ROUND", round)

    print(sorted(monkeyInspectedDictionary.values()))



    #check how many starting items



def readFile(inputFileName):
    file = open(inputFileName, 'r')
    lines = file.readlines()
    return lines

if __name__ == '__main__':
    main()



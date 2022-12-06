def main():
    day5()
    day5_2()


def day5():
    file1 = open('input7.txt', 'r')
    Lines = file1.readlines()
    numberOfStacks, numberLine = GetNumberOfStacks(Lines)
    #print(numberOfStacks, numberLine);

    stack = []
    for i in range(0,numberOfStacks):
        stack.append([])
    #print(stack)


    #Get all the cargo info
    for i in range(numberLine -2, -1, -1):
        #print(Lines[i])
        for x in range(0, numberOfStacks):
            if len(Lines[i]) >= 1+4*x:
                if not Lines[i][1+(4*x)] == " ":
                    stack[x].append(Lines[i][1+(4*x)])

    #print(stack)

    for line in Lines:
        if line.__contains__("move"):
            #Cleanup commands
            command =line.rstrip("\n")
            command = command.replace("move", "")
            command = command.replace("to", "")
            command = command.replace("from", "")
            command = command.lstrip(" ")
            #print(command)
            command = command.split("  ")
            command = [eval(i) for i in command]
            #print(command)

            #Move the crates
            for i in range(0, command[0]):
                if stack[command[1]-1]:
                    stack[command[2]-1].append(stack[command[1]-1].pop())

    print("===========================================")
    print("First stack top:")
    #print(stack)

    for i in range(0,numberOfStacks):
        print(stack[i][-1])
    print()


def day5_2():
    file1 = open('input8.txt', 'r')
    Lines = file1.readlines()
    numberOfStacks, numberLine = GetNumberOfStacks(Lines)
    #print(numberOfStacks, numberLine);

    stack = []
    for i in range(0,numberOfStacks):
        stack.append([])
    #print(stack)


    #Get all the cargo info
    for i in range(numberLine -2, -1, -1):
        #print(Lines[i])
        for x in range(0, numberOfStacks):
            if len(Lines[i]) >= 1+4*x:
                if not Lines[i][1+(4*x)] == " ":
                    stack[x].append(Lines[i][1+(4*x)])

    #print(stack)

    for line in Lines:
        if line.__contains__("move"):
            #Cleanup commands
            command =line.rstrip("\n")
            command = command.replace("move", "")
            command = command.replace("to", "")
            command = command.replace("from", "")
            command = command.lstrip(" ")
            #print(command)
            command = command.split("  ")
            command = [eval(i) for i in command]
            #print(command)

            #Move the crates
            betweenStack = stack[command[1]-1][-command[0]::]
            del stack[command[1]-1][-command[0]::]
            for x in betweenStack:
                stack[command[2]-1].append(x)
            #print("length", len(stack[command[1]-1])-command[0])
            #print(betweenStack)
            #stack[command[2]-1].append(["a", "b"])



    print("===========================================")
    print("Second stack top:")
    #print(stack)

    for i in range(0,numberOfStacks):
        print(stack[i][-1])


#Get's the number of stacks.
def GetNumberOfStacks(Lines):
    lineCounter = 0
    numberOfStacks = 1
    for line in Lines:
        lineCounter +=1
        if line.__contains__("1"):
            i = 1
            while True:
                if line.__contains__(str(i)):
                    i += 1
                else:
                    numberOfStacks = i - 1
                    return numberOfStacks, lineCounter

#=================================================


if __name__ == '__main__':
    main()

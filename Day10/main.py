

clock_cycle = 0
x_register = 1
signal_strength = 0

def main():
    global clock_cycle
    global x_register

    stringInput = readFile("input1.txt")

    for line in stringInput:
        if line.__contains__("noop"):
            clock_cycle += 1
            doClockCycle(clock_cycle,line)

        elif line.__contains__("addx"):
            line.replace("\n","")
            line = line.split(" ")
            clock_cycle += 1
            doClockCycle(clock_cycle, line)

            clock_cycle += 1
            doClockCycle(clock_cycle, line)
            x_register += int(line[1])

def doClockCycle(cycle, line):
    global signal_strength
    if (cycle-20) % 40 == 0:
        signal_strength += cycle * x_register
        print("cycle",cycle)
        print("x_register",x_register)
        print(line)
        print(signal_strength)

def readFile(inputFileName):
    file = open(inputFileName, 'r')
    lines = file.readlines()
    return lines

if __name__ == '__main__':
    main()



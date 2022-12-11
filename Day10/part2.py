

clock_cycle = 0
x_register = 1
signal_strength = 0
sprite_width = 3
line_array = [""]*40

def main():
    global clock_cycle
    global x_register

    stringInput = readFile("input1.txt")

    for line in stringInput:
        if line.__contains__("noop"):
            draw()
            clock_cycle += 1
            doClockCycle(clock_cycle,line)

        elif line.__contains__("addx"):
            line.replace("\n","")
            line = line.split(" ")
            draw()
            clock_cycle += 1
            doClockCycle(clock_cycle, line)

            draw()
            clock_cycle += 1
            doClockCycle(clock_cycle, line)
            x_register += int(line[1])

def draw():
    if (clock_cycle % 40) <= x_register+1 and (clock_cycle % 40) >= x_register-1:
        line_array[clock_cycle % 40] = "#"

    else:
        line_array[clock_cycle % 40] = "."

def doClockCycle(cycle, line):
    global signal_strength
    if (cycle) % 40 == 0:
        for x in line_array:
            print(x, end="")
        print()


def readFile(inputFileName):
    file = open(inputFileName, 'r')
    lines = file.readlines()
    return lines

main()



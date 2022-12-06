
def main():
    day4()
    day4_2()


def day4():
    file1 = open('input6.txt', 'r')
    Lines = file1.readlines()
    sum = 0

    for line in Lines:
        line = line.split(",")
        pairOne = line[0].split("-")
        line[1] = line[1].replace("\n","");
        pairTwo = line[1].split("-")
        #print(pairOne)
        #print(pairTwo)
        if int(pairOne[0]) <= int(pairTwo[0]) and int(pairOne[1]) >= int(pairTwo[1]):
            sum += 1;
        elif int(pairOne[0]) >= int(pairTwo[0]) and int(pairOne[1]) <= int(pairTwo[1]):
            sum += 1;
        #print("Sum:" + str(sum))
    print("Sum part 1: ", sum)

def day4_2():
    file1 = open('input6.txt', 'r')
    Lines = file1.readlines()
    sum = 0
    noOverlap =0

    for line in Lines:
        line = line.split(",")
        pairOne = line[0].split("-")
        line[1] = line[1].replace("\n","");
        pairTwo = line[1].split("-")
        #print(pairOne)
        #print(pairTwo)
        if int(pairOne[1]) < int(pairTwo[0]):
            noOverlap += 1;
        elif int(pairOne[0]) > int(pairTwo[1]):
            noOverlap += 1;
        else :
            sum += 1;
        #print("Sum:" + str(sum))
    print("Sum part 2: ", sum)


#=================================================


if __name__ == '__main__':
    main()

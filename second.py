#!/usr/bin/python3

import sys, re

def createNewFile(theta0, theta1):
    try:
        file = open("theta.py",'w+')
        file.write("theta0 = ")
        file.write(str(theta0))
        file.write("\n")
        file.write("theta1 = ")
        file.write(str(theta1))
        file.write("\n")
        file.close()
    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0)
    return

def calculLinearRegression(lstLeft, lstRight, lstPattern):
    sum0, sum1 = 0, 0
    tmpTheta0, tmpTheta1 = 0, 0
    learningRate, i = 0.1, 0
    # miss other loop
    while (i < len(lstLeft)):
        sum0 = (tmpTheta0 + (tmpTheta1 * lstLeft[i])) - lstRight[i]
        sum1 = ((tmpTheta0 + (tmpTheta1 * lstLeft[i])) - lstRight[i]) * lstLeft[i]
        tmpTheta0 -= learningRate * sum0
        tmpTheta1 -= learningRate * sum1
        i += 1
    i = 0
    print ("tmpTheta0: ", tmpTheta0)
    print ("tmpTheta1: ", tmpTheta1)
    print ("sum0", sum0)
    createNewFile(tmpTheta0, tmpTheta1)
    return

def createList(arg):
    lstLeft = []
    lstRight = []
    lstPattern = []
    file_object = open(arg, "r")
    lstObj = list(file_object)

    for line in lstObj:
        if (lstObj[0] == line):
            if (line.find(",") == -1):
                print ("Error line: ", line)
                exit(0)
            else:
                line = line[:line.find("\n")]
                split = line.split(',')
                if (len(split) == 2):
                    lstPattern.append(split[0])
                    lstPattern.append(split[1])
                else:
                    print ("Error line: ", line)
                    exit(0)
        else:
            if (re.search('^(\\d+),(\\d+)$', line) is None):
                print ("Error line: ", line)
                exit(0)
            match = re.match('^(\\d+),(\\d+)$', line)
            lstLeft.append(int(match.group(1)))
            lstRight.append(int(match.group(2)))
    return [lstLeft, lstRight, lstPattern]

def main():
    if (len(sys.argv) == 2):
        lst = createList(sys.argv[1])
        calculLinearRegression(lst[0], lst[1], lst[2])
        print (lst)
    elif (len(sys.argv) > 2):
        print ("Too few arguments")
    else:
        print ("Put one argument")

if __name__ == '__main__':
    main()

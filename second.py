#!/usr/bin/python3

import sys, re
import matplotlib.pyplot as plt

def display():
    # plt.scatter(lstLeft, lstRight, s = 15)
    # plt.title('ft_linear_regression')
    # plt.xlabel(lstPattern[0])
    # plt.ylabel(lstPattern[1])
    # plt.show()
    return

def calculLinearRegression(lstLeft, lstRight, lstPattern):
    tmp0 = 0
    tmp1 = 0
    theta0 = 0
    theta1 = 0
    learningRate = 0.1
    i = 0

    # miss learningRate (calcul gradient descent)
    # miss other loop
    while (i < len(lstLeft)):
        tmp0 = (theta0 + (theta1 * lstLeft[i])) - lstRight[i]
        tmp1 = ((theta0 + (theta1 * lstLeft[i])) - lstRight[i]) * lstLeft[i]
        theta0 = theta0 - (learningRate * tmp0)
        theta1 = theta1 - (learningRate * tmp1)
        i += 1
    i = 0
    print ("theta0: ", theta0)
    print ("theta1: ", theta1)


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

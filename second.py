#!/usr/bin/python3

import sys, re

def calculLinearRegression(lstLeft, lstRight):

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
            lstLeft.append(match.group(1))
            lstRight.append(match.group(2))
    return [lstLeft, lstRight, lstPattern]

def main():
    if (len(sys.argv) == 2):
        lst = createList(sys.argv[1])
        calculLinearRegression(lst[0], lst[1])
        print (lst)
    elif (len(sys.argv) > 2):
        print ("Too few arguments")
    else:
        print ("Put one argument")

if __name__ == '__main__':
    main()

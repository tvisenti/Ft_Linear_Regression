#!/usr/bin/python3

import sys, re

def createText(arg):
    lstPattern = []
    lstLeft = []
    lstRight = []
    file_object = open(arg, "r")
    lstObj = list(file_object)

    for line in lstObj:
        if (lstObj[0] == line):
            lstPattern.append(line[:line.find("\n")])
        else:
            if (re.search('^(\\d+),(\\d+)$', line) is None):
                print ("Error line: ", line)
                exit(0)
            match = re.match('^(\\d+),(\\d+)$', line)
            lstLeft.append(match.group(1))
            lstRight.append(match.group(2))
    return [lstPattern, lstLeft, lstRight]

def main():
    if (len(sys.argv) == 2):
        text = createText(sys.argv[1])
        print (text)
    elif (len(sys.argv) > 2):
        print ("Too few arguments")
    else:
        print ("Put one argument")

if __name__ == '__main__':
    main()

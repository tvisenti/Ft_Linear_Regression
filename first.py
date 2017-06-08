#!/usr/bin/python3

import sys, re

theta0 = 0
theta1 = 0

def main():
	if (len(sys.argv) == 1):
		km = input("Enter mileage: ")
		if (km.isdigit()):
			print (theta0 + (theta1 * int(km)))
		else:
			print ("Mileage is not a positive int")
	elif (len(sys.argv) > 1):
		print ("Too few arguments")

if __name__ == '__main__':
	main()

#!/usr/bin/python3

import sys, re
from theta import *

def main():
	if (len(sys.argv) == 1):
		km = input("Enter mileage: ")
		try:
			val = int(km)
			if (val < 0):
				print("That's not a positive int!")
				return
		except ValueError:
			print("That's not an int!")
			return
		result = (theta0 + (theta1 * int(km)))
		print ("Result: ", result)

	elif (len(sys.argv) > 1):
		print ("Too few arguments")

if __name__ == '__main__':
	main()

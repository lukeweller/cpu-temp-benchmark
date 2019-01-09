#!/usr/bin/python3
# Fixes error in which 100C prints empty value
import sys

if __name__ == '__main__':
	with open(sys.argv[1]) as f:
		file = f.read().split('\n')[:-1]

		for line in file:
			if line[0] == ',':
				line = '100' + line
			print(line)

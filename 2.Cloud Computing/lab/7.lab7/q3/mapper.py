#!/usr/bin/python

import sys

#with open('iris.data', 'r') as file:
    #data = file.readlines()

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # split the line into words
    words = line.lower().split(',')

    if words[0] != '':
        print(f"{words[:2]},1")

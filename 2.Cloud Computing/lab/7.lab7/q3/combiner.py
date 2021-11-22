#!/usr/bin/python

import sys
import math

words_dict = {}

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # split the line into words
    diff = line.split(',')
    points = list(map(lambda a: a.strip('[] '), diff))
    points = list(map(lambda a: float(a.strip("'")), points))

    a, b, count = points[0], points[1], int(points[2])

    dist = format(math.sqrt((a - b) ** 2), '.2f')
    word = dist

    if word in words_dict:
        words_dict[word] += ',1' * int(count)
    else:
        words_dict[word] = ' 1' + ',1' * (count - 1)

for k in sorted(words_dict.keys()):
    print(str(k) + words_dict[k])

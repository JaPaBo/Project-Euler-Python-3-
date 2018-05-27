# -*- coding: utf-8 -*-
"""
Solve Project Euler Problem 67 by importing from csv
"""
import csv
import numpy as np
import time
 
start = time.time()

list = []

#opens CSV and reads nonsquare entries into list of lists of strings
fh = open('prob67.csv', 'r')
for line in fh:
    list.append(line.strip().split(' '))

#converts all strings to numbers
for a in range(len(list)):
    for b in range(len(list[a])):
        list[a][b] = int(list[a][b])

#starting from next to last row, determining maximum path by summing each array entry with larger of two "lower" array entries
for c in range(len(list)-1):
    e = len(list)-2 - c
    for d in range(len(list[e])):
        list[e][d] += max(list[e+1][d],list[e+1][d+1])

#Calculating Solution Time
elapsed = (time.time() - start)

#Program output
print("Elapsed time: %f" % elapsed)
print("answer is: %f" % list[0][0])
 
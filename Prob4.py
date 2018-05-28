# -*- coding: utf-8 -*-
"""
Created on Sat May 26 23:22:32 2018

@author: JPBDell
"""

import math
import time
 
start = time.time()
max_palindrome = 0

def is_palindrome(palindrome):
    palindrome_string = str(palindrome)
    for i in range(len(palindrome_string)//2):
        if palindrome_string[i] != palindrome_string[len(palindrome_string)-1-i]:
            palindrome = 0
    return palindrome


for i in range(100,1000):
    for j in range (100,i):
        max_palindrome = max(max_palindrome, is_palindrome(i*j))


elapsed = (time.time() - start)

print("Solution is %i.  Calculated in %f seconds" % (max_palindrome, elapsed))
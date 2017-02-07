# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 21:08:26 2017
@author: John

Problem statement:
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

i=0
SoS = 0
Sum = 0

while i < 101:
    SoS = SoS + i**2
    Sum = Sum + i
    print(i**2, " ", SoS, " ", Sum)
    i = i+1
    
print("The answer is: ", Sum**2-SoS)
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 20:09:33 2017
@author: John

Project Euler Problem #1:
"If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."
"""


Sum = 0 #Holds running sum of natural numbers which are multiples of 3 v 5
i = 0   #integer used for while loop control

while i < 1000:
    if i%3 == 0:
        Sum = Sum + i
    elif i%5 == 0:
        Sum = Sum + i
    i = i+1

print("The answer is : ", Sum)

# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 21:08:58 2017
@author: John

Problem statement:
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

Fib_n2 = 0
Fib_n1 = 0
Fib_n0 = 1
Sum = 0


while Fib_n0 <= 4000000:
    if Fib_n0%2 == 0:
        Sum = Sum + Fib_n0
        print("adding to sum : ", Fib_n0)
    print(Fib_n0, " ", Fib_n1, " ", Fib_n2)   
    Fib_n2 = Fib_n1
    Fib_n1 = Fib_n0
    Fib_n0 = Fib_n1+Fib_n2
    
print("Final answer is: ", Sum)
   
    
    
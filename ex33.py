# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 06:45:52 2018

@author: jpmul
"""
print("-----------------------------------")
exercise_number = 33
print(f"Learn Python the Hard Way\nEx. {exercise_number} ({round((exercise_number/48.0)*100,1)}% complete)")
print("-----------------------------------\n")

def looper(n, increment):
    i = 0 
    numbers = []
    
    while i < n:
        print(f"At the top is i {i}")
        numbers.append(i)
        
        i += increment
        
        print("\tNumbers now: ", numbers)
        print(f"\tAt the bottom i is {i}")
    
    print("Outside of loop the numebrs: ")
    
    for num in numbers:
        print(num)
    
n = int(input("Loop how many times? "))
increment = int(input("Increment by? "))
looper(n, increment)


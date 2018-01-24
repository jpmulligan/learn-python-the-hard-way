# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 07:40:41 2018

@author: 40261
"""

print("LPTHW exercises complete: ", round((30.0/48.0)*100,1),"%")

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
    
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
    
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
    
    
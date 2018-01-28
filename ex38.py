# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 20:01:17 2018

@author: jpmul
"""

print("-----------------------------------")
exercise_number = 38
print(f"Learn Python the Hard Way\nEx. {exercise_number} ({round((exercise_number/48.0)*100,1)}% complete)")
print("-----------------------------------\n")

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn",
              "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ",  next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do things to stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
     
      
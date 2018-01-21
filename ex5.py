# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 07:06:37 2018

@author: jpmul
"""

name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #pounds

#convert convert!
height = round(height * 2.54)
weight = round(weight / 2.2) #kg

eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} cm tall.")
print(f"He's {weight} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")


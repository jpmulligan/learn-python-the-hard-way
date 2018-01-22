# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 20:59:53 2018

@author: jpmul
"""

print("LPTHW exercises complete: ", round((16.0/48.0)*100,1),"%")

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want to do that, hit CTRL-C now.")
print("If you do want to do that, hit ENTER")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ") + "\n"
line2 = input("line 2: ") + "\n"
line3 = input("line 3: ") + "\n"

print("I'm going to write these to the file.")

target.write(line1 + line2 + line3)

print("And finally, we close it.")
target.close()


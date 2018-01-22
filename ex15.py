# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 20:48:32 2018

@author: jpmul
"""

print("LPTHW exercises complete: ", round((15.0/48.0)*100,1),"%")

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
txt.close()


print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()


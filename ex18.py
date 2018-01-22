# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:20:53 2018

@author: 40261
"""

print("LPTHW exercises complete: ", round((18.0/48.0)*100,1),"%")

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    
# ok that * args is pointless we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothing.")

print_two("monkey", "banana")
print_two_again("monkey", "banana")
print_one("FP!")
print_none()


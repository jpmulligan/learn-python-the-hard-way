# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:28:53 2018

@author: 40261
"""

print("LPTHW exercises complete: ", round((19.0/48.0)*100,1),"%")

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party")
    print("Get a blanket.\n")

print("We can just give the function numbers directly.")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too!")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

def aoc(diam):
    area = 3.1415927 * (diam/2)**2
    print(f"Area = {area}")

aoc(2)
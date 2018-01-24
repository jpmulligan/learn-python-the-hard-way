# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:12:05 2018

@author: jpmul
"""

print("LPTHW exercises complete: ", round((29.0/48.0)*100,1),"%")

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! World doomed!")

if people > cats:
    print("World saved")
    
if people < dogs:
    print("The world is drool.")

if people > dogs:
    print("The world is dry.")
    
    
dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("peep less than or equal to dogs")

if people == dogs:
    print("people are dogs")
    
    
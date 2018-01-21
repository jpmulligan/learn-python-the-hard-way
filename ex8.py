# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 12:09:11 2018

@author: jpmul
"""

print("LPTHW exercises complete: ", round((8.0/48.0)*100,1),"%")

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
        "Try your",
        "Own text here",
        "Maybe a poem",
        "Or a song about fear"
))


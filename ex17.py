# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:08:30 2018

@author: 40261
"""

print("LPTHW exercises complete: ", round((17.0/48.0)*100,1),"%")

from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print(f"Copying from {from_file} to {to_file}")

indata = open(from_file).read()

#print(f"The input file is {len(indata)} bytes long.")
#print("Ready, hit ENTER to continue, CTRL-C to abort.")
#input()

out_file = open(to_file, 'w')
out_file.write(indata)

#print("Alright, all done!")
print(f"Copied {from_file} to {to_file}, {len(indata)} bytes")

out_file.close()





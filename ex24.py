# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:52:43 2018

@author: jpmul
"""

print("LPTHW exercises complete: ", round((24.0/48.0)*100,1),"%")

print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("------------------")
print(poem)
print("------------------")

five = 10-2+3-6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

#another way to format
print("With a starting point of: {}".format(start_point))

#its just like with an f string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

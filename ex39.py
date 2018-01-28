# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 20:13:22 2018

@author: jpmul
"""

print("-----------------------------------")
exercise_number = 39
print(f"Learn Python the Hard Way\nEx. {exercise_number} ({round((exercise_number/48.0)*100,1)}% complete)")
print("-----------------------------------\n")

states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
        }

cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
        }

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

print(states['Michigan'])

print(cities[states['Michigan']])

print(states)
print(states.items())
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

state = states.get('Florida')
print(state)

if not state:
    print("Sorry, no Texas")

city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")

    
    
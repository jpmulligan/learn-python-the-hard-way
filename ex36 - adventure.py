# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 07:37:14 2018

@author: jpmul
"""

import csv
from sys import exit

map = []

print("Loading map...")
with open('map.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for room in reader:
        print(room['ID'], room['RoomName'])
        map.append(room)

print(f"Map loaded with {len(map)} rooms. Game on\n\n")


HP = 100
starting_room = "100"
prompt = '> '

def view_room(room_id):
    #print("Viewing room...")
    for room in map:
        #print("Checking... ", room['ID'])
        if room['ID'] == room_id:
            print(f"\n\n[ {room['RoomName']} ]")
            print(room['Descrip'])
            #print(room['N'])
            return
    print(f"view_room failed trying to find {room_id}")
    exit(1)

current_room = starting_room

while HP > 0:
    #print("Current room, main loop = ", current_room)
    view_room(current_room)
    
    action = input(prompt)
    action = action.upper().split()
    verb = action[0]
    
    if verb == "EXIT":
        print("GAME OVER!")
        exit(0)
    
    elif verb == "GO":
        direction = action[1]
        #print("direction = ", direction)
        #print("Current room = ",current_room)
        for room in map:
            #print(current_room, room['ID'], room['RoomName'])
            if room['ID'] == current_room and int(room[direction]) > 0:
                #print("ID match, ",room[direction])
                #print("Setting room to ", room[direction])
                current_room = room[direction]
                break
        else:
            print("You can't go that way.")
    
    else:
        print("Unrecognized command")
        
    




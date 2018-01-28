# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 20:25:51 2018

@author: jpmul
"""

print("-----------------------------------")
exercise_number = 40
print(f"Learn Python the Hard Way\nEx. {exercise_number} ({round((exercise_number/48.0)*100,1)}% complete)")
print("-----------------------------------\n")

class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

hbd = Song(['Happy b day', 'I dont want to get sued', 'so i will stop there'])
bop = Song(['They rally around tha family', 'with a pocket full of shells'])

hbd.sing_me_a_song()

bop.sing_me_a_song()



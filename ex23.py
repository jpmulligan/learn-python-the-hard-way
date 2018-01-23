# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:20:40 2018

@author: jpmul
"""

print("LPTHW exercises complete: ", round((23.0/48.0)*100,1),"%")

import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
    
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    
    print(raw_bytes, "<===>", cooked_string)
    
languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)


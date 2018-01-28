# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:22:12 2018

@author: jpmul
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = "World"
    return f'Hello, {greeting}!'

if __name__ == "__main__":
    app.run()
    
    
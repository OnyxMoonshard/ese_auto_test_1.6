# !/usr/bin/python3


import os

currentDir = os.path.abspath(os.path.dirname(__file__))
print("current:"+currentDir)
proDir = os.path.split(currentDir)[0]
print("proDir:"+proDir)
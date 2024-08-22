# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 07:55:19 2024
@author: segal
"""
#Clip:
    # cntDown Timer:
import time

# ask user for a timeLimit:
AsetTime = int(input("Give me a time you want to set in seconds: "))

# and cnt backwards using a step:
    
for x in range(AsetTime, 0, -1):
    seconds = x % 60 # for the remainder and seeing a display
    minutes = int( x / 60 ) % 60
    hours = int( x/ 3600 ) % 24 # but not needed to see days
    print(f"{hours:02}:{minutes:02}:{seconds:02}") # and for formate padding seconds:02
    time.sleep(1)

print("Time is up!")        

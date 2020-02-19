#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:22:46 2020

@author: prasanthchakka
"""

import csv

import json

#%%

# reading files
with open("output.csv") as f:
    reader = csv.reader(f)
    
    for line in reader:
        print(line[0])
        
#%%    
        
lines = [["asdf","hello"],["pfdnfj","world"]]

with open("written_csv.csv","w") as f:
    write = csv.writer(f)
    
    for line in lines:
        write.writerow(line)
        
#%%
#writing dictionaries
        
beatles = [
    {"name": "John", "instrument": "voice"},
    {"name": "Paul", "instrument": "guitar"},
    {"name": "George", "instrument": "bass"},
    {"name": "Ringo", "instrument": "drums"}
]

with open("beatles.csv", "w") as my_file:
    writer = csv.DictWriter(my_file, ["name", "instrument"])
    writer.writeheader()
    for beatle in beatles:
        writer.writerow(beatle)
        
#%%
    #Reading with column names
with open("beatles.csv") as my_file:
    reader = csv.DictReader(my_file)
    for beatle in reader:
        print(beatle["name"] + " -> " + beatle["instrument"])

#%%

  


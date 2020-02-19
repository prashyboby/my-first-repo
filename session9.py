#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:33:36 2020

@author: prasanthchakka
"""
#%%
#opening files 

file = open("/Users/prasanthchakka/Desktop/my-first-repo/text_file.txt")

for line in file:
    print(line)
    
file.close()
    
#%%
#With usage

with open("/Users/prasanthchakka/Desktop/my-first-repo/text_file.txt") as file1:
    for line in file1:
        print(line)
        
        
#%%
        
test = " Just kidding"

with open("/Users/prasanthchakka/Desktop/my-first-repo/text_file.txt","w") as file:
    file.write(test)
    print(file)
#%%
# Exercises
my_csv = open("/Users/prasanthchakka/Desktop/my-first-repo/sample.csv")

def from_csv(my_csv):
    my_list = []
    for line in my_csv:
        my_cells = line.split(",")
        my_list.append(my_cells)
        
    return my_list


print(from_csv(my_csv))

my_csv.close()



def to_csv(my_list):
    with open("output.csv","w") as file:
        for line in my_list:
            line_as_string = ",".join(line)+"\n"
            file.write(line_as_string)
            
to_csv([["Hola","Hello"],["Adios","Bye"]])
        
   
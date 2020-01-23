#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 08:29:04 2020

@author: prasanthchakka
"""

#%%
def area_of_square(side):
    return side ** 2
    #area = side ** 2
    #print(area)

area=area_of_square(5)
print(area)

type(4.3) == float



#%%


def input_type_func(side):
    #print(type(side))
    if type(side) == float or type(side) == int:
        print("Type is float \n")
    else :
        print("Neither float nor int")
    
input_type_func(4.3)

#%%
def calculate_time():
    daily_time = float(input("Please provide your average daily commute time: "))
    return 7 * daily_time

#%%

True or 11 > 34





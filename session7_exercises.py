#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 08:34:20 2020

@author: prasanthchakka
"""

#%%
def my_func():
    i = 0
    my_list=[]
    
    while(i < 500):
        my_list.append(i+1)
        i+=1
        
    return my_list

my_func()
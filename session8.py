#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 09:00:03 2020

@author: prasanthchakka
"""

#%%
beatles = {
 "John"  : "sings",
 "Paul"  : "plays bass",
 "Ringo" : "plays drums",
 "George": "plays guitar"        
}

beatles = {}

beatles["John"] = "sings"
beatles["Paul"] = "plays bass"

beatles.pop("Paul")

#%%

beatles.keys()
beatles.values()


#%%

for i in beatles:
    print(i + " " + beatles[i])
    
#%%
#SETS
    
beatles = {"John","Paul","George","Ringo"}

numbers = set([1,2,2,2,3,3,3,4,5,5,6])
print(numbers)

#%%
#adding and removing
numbers = set([1,2,2,2,3,3,3,4,5,5,6])

numbers.add(7)

numbers

#discard vs remove

numbers.discard(5)
numbers.discard(5)
numbers.remove(5)

another = {2,3}

#%%

for i in numbers:
    print(i)
    
#%%


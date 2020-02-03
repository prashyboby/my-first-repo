#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 08:36:23 2020

@author: prasanthchakka
"""

#%%

beatles = ["Ringo","John","George","Paul"]

print(beatles)

empty_list = []

two_dim_list = [[1,2,3],[4,5,6],3]

print(two_dim_list)

print(two_dim_list[0][1])

print(beatles[1])

#%%

number = [1,2,3]

numbers_1 = number + [4,5,6]

mul = number * 3

print(mul)

print(numbers_1)

#%% mutating the list values

two_dim_list[1] = 2 

print(two_dim_list)

two_dim_list.index(2)

two_dim_list.append(5)

two_dim_list.append("Who am I")

two_dim_list = ["Please"] + two_dim_list

print(two_dim_list)

#%%

beatles.insert(1,"PC")

print(beatles)

beatles.remove("PC")

#%%

beatles.pop(2)

#%% Iterations

for i in beatles:
    print(i+" was a member of the Beatles")


#%%

two_d_list = [[1,2,3],[4,5,6]]
sum = 0
for l in two_d_list:
    for num in l:
        sum = sum + num

print(sum)

#%%
while False:
    print("Hello Dolly")
    
#%%
len(beatles)

#%%
acc = 0
i = 0

while i < len(two_d_list):
    j = 0
    while j < len(two_d_list[i]):
        acc = acc + two_d_list[i][j]
        j += 1
    i += 1    
    
print(acc)

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:16:43 2020

@author: AMISHA NARSINGANI
"""
my_list = [10,20,10,30,40,10,20,50,20,40,50,20,10,30,40]
frequencies = {} 
  
for i in my_list: 
    if i in frequencies: 
        frequencies[i] += 1
    else: 
        frequencies[i] = 1
print("My List:",my_list)       
print("Frequencies of elements :", frequencies)

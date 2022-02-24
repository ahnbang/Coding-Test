# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 16:21:01 2022

@author: AHN-BYOUNG-JOON
"""
# First Solution => time : 5.663890361785889
N = int(input())
orders = input().split()

def MoveProcess(mapsize, orders): 
    
    orders = list(orders)
    CP = [1,1]
    
    for order in orders:
        
        if order == 'L' and CP[0] != 1:
        
            CP[0] -= 1
    
        elif order =='R' and CP[0] != mapsize:
            
            CP[0] += 1
            
        elif order == 'U' and CP[1] != 1:
            
            CP[1] -= 1
            
        elif order == 'D' and CP[1] != mapsize:
            
            CP[1] += 1
            
    CP[0],CP[1] = CP[1], CP[0] # Questions want (column, row) 
    return CP

print(MoveProcess(N, orders))
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


S=[]
t=int(input())
for i in range(t):
    i=int(input())
    S.append(i)

Z=[]
for i in range(1,1667):
    if i%3!=0 and i%10!=3:
        Z.append(i)
        
for i in range(0,len(S)):
    print(Z[S[i]-1])
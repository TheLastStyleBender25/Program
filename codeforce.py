# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 17:39:48 2021

@author: dell
"""
def RedBlue(a):
    if len(a)==1:
        if a[0]=='R' or a[0]=='B':
           ass = ''.join(map(str,a))
           return ass
        else:
           a[0]='R'
           ass = ''.join(map(str,a))
           return ass
    
    l=len(a)
    count=0
    for i in range(0,len(a)):
        if a[i]=='?':
            count=count+1
    if count == l:
        for i in range(0,len(a)):
            if a[i-1]=='R':
                a[i]='B'
            else:
                a[i]='R'
       
    s1=s2=0 
    for i in range(0,len(a)):
        if a[i]=='R':
            s1=i
            break
        elif a[i]=='B':
            s2=i
            break
    if s2!=0:      
     for i in range(s2-1,-1,-1):
        if a[i+1]=='R':
            a[i]='B'
        else:
           a[i]='R'
           
    else:       
     for i in range(s1-1,-1,-1):
        if a[i+1]=='R':
            a[i]='B'
        else:
            a[i]='R'
            
    for i in range(0,len(a)):
        if a[i]=='?':
            if a[i-1]=='B':
                a[i]='R'
            elif a[i-1]=='R':
                a[i]='B'

    atostr = ''.join(map(str,a))
   # print(atostr)
    return atostr      

t=int(input())
z=[]
for i in range(t):
    s=int(input())
    a=input()
    a=list(a)
    ss=RedBlue(a)
    #print(ss)
    z.append(ss)
# print('now')
for q in range(0,len(z)):
        print(z[q])

    
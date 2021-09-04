# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 02:53:05 2021

@author: Shrey Arya
"""
def mod(a,b):
    ans1=b%a
    ans2=int((b+1)/2)
    #print(ans2)
    
    if ans2<a:
        ans2=0
        print(ans1)
    else:
        ans2=ans2-1
        print(ans2)



t=int(input())
z=[]
ss=[]
for i in range(t):
    a,b=map(int,input().split())
    if a>b:
        temp=b
        b=a
        a=temp
    mod(a,b)

# for i in range(0,len(ss)):
#     print(ss[i])
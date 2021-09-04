# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:27:58 2021

@author: Shrey Arya
"""
t= int(input())
f=[]
for i in range(t):
    q=int(input())
    f.append(q)
row=0
col=2
s=10
T=[[1,2,5],[4,3,6],[9,8,7]]

def dis(i):
    for w in range(0,len(T)):
        for e in range(0,len(T[w])):
            if T[w][e]==i:
                print(i)
                print(w,'',e)

def impt(row,col,s):
    #print('row', row)
    for i in range(col,-1,-1):
     T[row].insert(i,s)
     #print(i,s)
    # print(T[row])
     s=s+1
     T[row].sort()
     T[row].reverse()
    row=row+1
    #print('closed')
    return s
            

# for i in range(0,len(T)):
#     for j in range(0,len(T)):
#         print(T[i][j], end=" ")
#         # print('i and j',i,j)
#     print()
n=0
while n<300:
 row=0
 for i in range(0,len(T)): 
    for j in range(0,len(T)):
       #print(i,j)
       if i== row and j==col:
       #     T.insert(j+1,s)
               #print(row,col)
               #print('s is',s)
               T[row].insert(col+1,s)
               row=row+1
               s=s+1
               #print(row,col)

               
 T.append([s])
 s=impt(row,col,s+1)       
 col=col+1 
 #print('next')
 #print(len(T))
 n=n+1

print(T)

for i in range(0,len(f)):
    dis(f[i])






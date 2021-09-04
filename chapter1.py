# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 13:21:45 2021

@author: Shrey Arya
"""

def Connie(s):
    z=[]
    x=[]
    s=list(s)
    if len(s)==1:
        print(0)
        return 
    
    for i in range(0,len(s)):
        #print(s[i])
        #print(s.count(s[i]))
        z.append(s.count(s[i]))
    #print(z)
    x=z
    x.sort()
   # print(max(x))
    for i in range(0,len(z)):
        if z[i]==max(z):
           # print(z[i],s[i])
            break
    c=z[i]
    w=len(z)-c
    #print(c,w)
    v=0
    co=0
    vo=[]
    con=[]
    for i in range(0,len(s)):
            
        if s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
            v+=1
            vo.append(s[i])
        else:
            co+=1
            con.append(s[i])
    # print('v and co',v,co)
    # print(vo,con)
    
        
    maxx=0
    temp=1
    if len(con)!=0:
     for i in range(0,len(con)):  #FOR CONSONENT LIST
        temp=con.count(con[i])
        if maxx<temp:
            maxx=temp
            temp=0
            #print(con[i])
        if temp==0:
            #print(con[i])
            alpha=con[i]
     #print(alpha)
    else:
        alpha=0
    #print(maxx)
    if maxx==1:
        maxx=0
    minm=len(con)-maxx
    #print(minm)
    
    vmax=0
    if len(vo)!=0:
     for i in range(0,len(vo)):      #FOR VOWEL LIST
        temp=vo.count(vo[i])
        if vmax<temp:
            vmax=temp
            temp=0
        if temp==0:
            sigma=vo[i]
     #print(sigma)
    else:
        sigma=0
    #print(vmax)
    # print("len of v",len(vo))
    # print("len of c",len(con))
    count=0
    vount=0
    
    for i in range(0,len(con)):
        if con[i]==alpha:
            pass
        else:
            count+=2
    # print('count',count)
    # print('after all',count+len(vo))
    

        
    
    for j in range(0,len(vo)):
        if vo[j]==sigma:
            pass
        else:
            vount+=2
    # print('vount',vount)
    # print('after all',vount+len(con))
    
    if (count+len(vo)) < (vount+len(con)):
        print(count+len(vo))
        return
    else:
        print(vount+len(con))
        return
   
    

t=int(input())
for i in range(t):
    s=input()
    Connie(s)

# -*- coding: utf-8 -*9-
"""
Created on Wed Aug 25 13:37:54 2021

@author: Shrey Arya
"""
import math

dic=[1,2,4,8,16,32,64,128,256,512,1024]

def fact(num):
 while num % 2 == 0:  
       # print(2,)  
        z.append(2)
        num = num / 2  
  
 for i in range(3, int(math.sqrt(num)) + 1, 2):  
   
        while num % i == 0:  
            #print(i,)  
            z.append(i)
            num = num / i  
 if num > 2:  
        #print(int(num))
        z.append(int(num))
            
n=812
z=[]
for i in range(0,84):
    if 2**i <=n and 2**(i+1) >n:
        #print(i)
        break
s=2**i

if n==s:
    print('no change')

fact(n)

som=0
for i in range(0,len(z)):
    som=som+z[i]
    if som in dic:
       # print('yes')
        break

n=list(map(int, str(n)))
s=list(map(int,str(s)))

def check(n,count):
 for i in range(0,len(s)):
    if s[i]!=n[i]:
        flag=s[i]
        count=count+1
        #print('count',count)
        #print(flag)
        break
 if n==s:
    # print(count)
     d.append(count*2)
     return
 n.pop(i)
 for i in range(0,4):
  if len(n)!=0:
   no=int(''.join(map(str,n)))
   #print('n is',no)
   if 2**i == no:
    print('yes')  
    return no      
 n.insert(i,flag)
 check(n,count)
flag=0
count=0
d=[]
check(n,count)












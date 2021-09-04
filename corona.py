# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#print("enter the test case")
no=int(input())
print(no)
#print('enter the cases')
#for i in range(1,no+1):
    #print(i)
    
#data=[11,10,5,8,15]
total=0
#print(data.index(15))
#print(sorted(data))
#for i in data:
    #print(i, end=' ')
    #total=total+i

#print('\n', total)    
#for i in data:
   # if i < total:
       # total=i
#print(min(data))
#for i in range(4):
    #print(data[i+1]+1)

#datacp=data[:]
#for i in data:
 #   for j in range(0,len(data)-1):
  #     if data[j]>data[j+1]:
   #         ss=data[j]
    #        data[j]=data[j+1]
     #       data[j+1]=ss

#print(data)


dr=[]
#for i in range(no):
 #   el=int(input())
  #  dr.append(el)
#print(dr)
#print(sorted(dr))
#print(dr.index(55))
#print()
#for i in range (len(dr)):
    #for j in range(0,len(dr)-1):
   #     if dr[j]>dr[j+1]:
  #        ss=dr[j]
 #         dr[j]=dr[j+1]
#          dr[j+1]=ss

#print(dr);
cr="corona"
asa = list(cr)
print("corona")
for i in range(no):
    el=input()
    dr.append(el)
    
print(dr)
     
for i in range(0, len(dr)):

    for j in range(0,len(dr[i])):
        for z in range (0,6):
           # print('value of dr', dr[i][j])
           # print('value of asa', asa[z])
            if dr[i][j] == asa[z]:
                total=total+1
               # print("y")
            #else:
               # print('n')
        #print(total)
        
    if total >= 1:
            print( dr[i])
    total=0


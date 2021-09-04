# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 23:00:55 2021

@author: dell
"""
amount=0
f=open('shreyaccount.txt','r+')

class bankss:
    
    
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance

        
    def bal(self):
        print(f'current balance is: {self.balance}')
        
    def add(self):
        amount=float(input('amount to be added:  '))
        self.balance+=amount
        print('balance is: ',self.balance)
        f.seek(0)
        f.truncate(0)
        f.write(str(self.balance))
        
        print(f'balance is {self.balance}')

    def withdraw(self):
        amount=float(input('amount to be withdraw:  '))
        if self.balance < amount :
            print(f'balance is less to to cash {self.balance}')
        else:
            self.balance -= amount
            print(f'balance is {self.balance}')
            f.seek(0)
            f.truncate(0)
            f.write(str(self.balance))

s=f.read()
s=float(s)
suja= bankss('rumi',s)
suja.bal()
inv = int(input('enter 1 to add or 2 to withdraw or 3 to check balance: \n'))

if inv == 1:
    suja.add()
    f.close()
elif inv == 3:
    suja.bal()
else:
    suja.withdraw()
    f.close()
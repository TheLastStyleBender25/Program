# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 20:59:36 2021

@author: dell
"""

class Patient(object):
    
    status='patient'
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.condition=[]
        
    def get_details(self):
        print(f'patient name {self.name},age is {self.age}, information: {self.condition}')
        
    def add_info(self,information):
        self.condition.append(information)
        
# shrey= Patient('shrey kumar', 28)
# annissa= Patient('annissa garcia',24)

class Infant(Patient):
    
    def __init__(self, name, age):
        self.vaccination=[]
        super().__init__(name, age)
        
    def add_vac(self,vaccine):
        self.vaccination.append(vaccine)
        
    def get_details(self):
        print(f'patient record: name is {self.name}, age is {self.age}, information {self.condition}, has vaccine: {self.vaccination}')
        
        
rumi=Infant('rumi',18)
rumi.add_vac('MVR')
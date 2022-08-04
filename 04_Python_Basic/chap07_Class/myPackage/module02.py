# -*- coding: utf-8 -*-
"""
module02.py
"""
class calculation:
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    # ADD
    def add(self):
        print('Add=',self.a+self.b)
    # SUB
    def sub(self):
        print('Sub=',self.a-self.b)
    # MUL
    def mul(self):
        print('Mul=',self.a*self.b)
    # DIV
    def div(self):
        print('Div=',self.a/self.b)

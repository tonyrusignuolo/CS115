'''
Created on Nov 27, 2017

@author: arusignu
'''

from shape import *

class Triangle(Shape):
    def __init__(self,x,y,base,height,name = 'Triangle'):
        super().__init__(x,y,name)
        self.__base = base
        self.__height = height
        
    @property
    def base(self):
        return self.__base
    
    @property
    def height(self):
        return self.__height
    
    @base.setter
    def base(self,base):
        self.__base = base
        
    @height.setter
    def height(self,height):
        self.__height = height
        
    @property
    def area(self):
        return (self.__base * self.__height) / 2
    
    def __str__(self):
        return super().__str__() + ', base = ' + str(self.__base)
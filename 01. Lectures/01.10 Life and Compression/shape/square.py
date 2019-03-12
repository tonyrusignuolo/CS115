'''
Created on Nov 27, 2017

@author: arusignu
'''

from rectangle import *

class Square(Rectangle):
    def __init__(self, x, y, length, name='Square'):
        super().__init__(x, y, length, length, name)
'''
Created on Sep 14, 2017

@author: arusignu
'''

from cs115 import map, reduce

def dbl(x):
    """Returns twice the input x.
        input x: a number (int or float)"""
    return 2 * x

mylist = range(1, 5)
print(mylist)
newlist = map(dbl, mylist)
print(newlist)
print(mylist)
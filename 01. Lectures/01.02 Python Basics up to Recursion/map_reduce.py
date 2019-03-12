'''
Created on Jan 27, 2015
Last modified on Jan 23, 2016

@author: Brian Borowski

CS115 - Examples of map-reduce
'''
from cs115 import map, reduce

def mult(a, b):
    '''Returns the product of a and b.'''
    return a * b

def add(a, b):
    '''Returns the sum of a and b.'''
    return a + b

def sqr(x):
    '''Returns the square of x.'''
    return x * x

def span(lst):
    '''Returns the difference between the maximum and minimum numbers in a
    list'''
    return reduce(max, lst) - reduce(min, lst)

def gauss(n):
    '''Takes as input a positive integer n and returns the sum
    1 + 2 + 3 + ... + n'''
    return reduce(add, range(1, n + 1))

def sum_of_squares(n):
    '''Takes as input a positive integer n and returns the sum
    1^2 + 2^2 + 3^2 + ... + n^2'''
    return reduce(add, map(sqr, range(1, n + 1)))

print(map(sqr, range(1, 4)))

"""
list_of_strings = ['hello', 'my', 'name', 'is', 'brian']
print(map(len, list_of_strings))

list_of_ints = [1, 2, 3, 4, 5]
print(reduce(mult, list_of_ints))

print(span([3, 1, 42, 7, -1]))
print(gauss(10))
print(sum_of_squares(10))
"""
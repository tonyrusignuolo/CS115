'''
Created on Sep 13, 2017

@author: arusignu
'''

from cs115 import map, reduce, filter

def mult(x, y): 
    """Returns the product of x and y""" 
    return x * y

def add(x, y):
    """Returns the sum of x and y."""
    return x + y

def sum(L):
    """Returns the sum of a list, L."""
    return reduce(add, L)

def mean(L):
    """Returns the average value of a list, L."""
    return sum(L)/len(L)

def factorial(n):
    """Returns the factorial of a given number, n."""
    if n==0:
        return 1
    return n*factorial(n-1)
    
def divides(n):
    def div(k):
        return n % k == 0
    return div

def prime(n):
    """Returns whether the integer n is prime or not."""
    return sum(map(divides(n),range(1,n+1))) == 2
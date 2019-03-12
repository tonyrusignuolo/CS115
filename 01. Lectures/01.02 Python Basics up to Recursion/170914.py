'''
Created on Sep 14, 2017

@author: arusignu
'''

from cs115 import map, reduce
 
def tower(n):
    """Computes 2^(2^(2...)) with n twos, using recursion."""
    if n==0:
        return 1
    return 2 ** tower(n-1)
 
def tower_reduce(n):
    def power(x, y):
        return y ** x
    if n==0:
        return 1
    return reduce(power, [2] * n)
 
def length(lst):
    """Returns the length of the list."""
    if lst == []:
        return 0
    return length(lst[1:])
    
def reverse(lst):
    """Takes as input a list of elements and returns the list in reverse order."""
    if lst == []:
        return []
    return reverse(lst[1:]) + [lst[0]]

def member(x, lst):
    """Returns true if x is contained in the list and false otherwise."""
    if lst ==[]:
        return False
    if x == lst[0]:
        return True
    return member(x, lst[1:])

def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y - 1)

def power_tail(x,y):
    """Returns the exponent x^y."""
    def power_tail_helper(x,y,accum):
        if y == 0:
            return accum
        return power_tail_helper(x, y - 1, x * accum)
    return power_tail_helper(x,y,1)

def mystery(n):
    return m_help(n,0)

def m_help(n,r):
    """Returns the mirror of most intergers, n."""
    if n == 0:
        return r
    return m_help(n // 10, r * 10 + n % 10)

def my_map(f, lst):
    """"""
    if lst ==[]:
        return []
    return [f(lst(0))] + my_map(f, lst[1:])

def my_reduce(f, lst):
    def my_reduce_helper(f, lst, accum):
        if lst==[]:
            return accum
        return my_reduce_helper(f, lst[1:], f(lst[0], accum))
    if lst ==[]:
        raise TypeError('my_reduce() of empty sequence with no initial value')
    return my_reduce_helper(f, lst[1:], lst[0])
'''
Created on Sep 12, 2017
 
@author: arusignu
'''

from cs115 import map, reduce
 
def tower(n):
    """Computes 2^(2^(2...)) with n twos, using recursion."""
    if n==0:
        return 1
    return 2 ** tower(n-1)
 
print (map(tower, range(5)))

def tower_reduce(n):
    def power(x, y):
        return y ** x
    if n==0:
        return 1
    return reduce(power, [2] * n)
 
print(tower_reduce(0))

def length(lst):
    """Returns the length of the list."""
    if lst == []:
        return 0
    return length(lst[1:])
    
print(length([1, 2, 3]))

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

print(reverse([1,2,3,4]))

def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y - 1)


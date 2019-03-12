'''
Created on Sep 27, 2017

@author: arusignu
'''

from cs115 import *

#1
L = ['Why', 'is', 'it', 'raining']
M = ['How', 'now', 'brown', 'cow']
N = L[:2] + [L[-1]] + M[3:]

print(N)
#ans = ['Why', 'is', 'raining', 'cow']

#2
M = range(3,5)

print(M)
#'is'

#3

#ans = [7, 'stevens']

#4

"""
ansa = 3
ansb = (a) tail
ansc = 10,2
ansd = 2
"""

#5
"""
ansa = 8
ansb = tree
ansc = 'annoy'
ansd = 'yonna'
"""

#6
"""
ansa = []
ansb = lst[0]
ansc = [lst[0]]
ansd = 1
anse = min_length
ansf = lst[1:]
ansg = min_length
ansh = filter(lambda x: len(x) >= min_length,lst)
"""

#7
' Question 7 (20 points) 
' Implement these functions using recursion. 
def keep_integers(lst): 
    """
    Assume lst is a list of all different data types. There could be ints, 
    floats, strings, booleans, nested lists, and more. 
    Return a list of only the integers present in the original list. You do 
    not have to worry about integers inside nested lists and can safely 
    ignore them. 
    You may use type(data) == int to determine if the data variable is an 
    integer. 
    This part is worth 20 points.
    """ 
    if lst == []:
        return []
    if type(lst[0]) == int:
        return [lst[0] + keep_integers(lst[1:])]
    return keep_integers(lst[1:])
        
#8
' Question 8 (10 points) 
' Implement this function using the Pythons built-in filter and lambda. 
' DO NOT USE recursion. 
 
def keep_integers_filter(lst): 
    '''Assume lst is a list of all different data types. There could be ints, 
    floats, strings, booleans, nested lists, and more. 
    Return a list of only the integers present in the original list. You do 
    not have to worry about integers inside nested lists and can safely ignore them. 
    You may use type(data) == int to determine if the data variable is an 
    integer. 
    This part is worth 10 points.'''
    return filter(lambda x: type(x) == int, lst)
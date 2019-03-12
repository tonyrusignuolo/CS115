'''
Created on Sep 14, 2017

@author: arusignu
'''

from cs115 import map, reduce, filter
from functions import mult

def dot(L, K):
    """Returns the dot product of the two lists L and K."""
    if L == [] or K == []:
        return 0
    return L[0]*K[0] + dot(L[1:],K[1:])

def explode(S):
    """"Returns a list of all the characters in the string S."""
    if S == "":
        return []
    return [S[0]] + explode(S[1:])

def ind(e, L):
    """Returns the position of element e in the list or string L."""
    if L==[] or L=="":
        return 0
    if e==L[0]:
        return 0
    return 1 + ind(e,L[1:])

def removeAll(e,L):
    if L==[]:
        return []
    if e==L[0]:
        return removeAll(e,L[1:])
    return [L[0]] + removeAll(e,L[1:])

def even(X):
    if X % 2 == 0:
        return True
    return False

def myFilter(f, L):
    if L==[]:
        return []
    if f(L[0])==True:
        return [L[0]] + myFilter(f,L[1:])
    return myFilter(f,L[1:])

def deepReverse(L):
    if L==[]:
        return []
    if isinstance(L[0],list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    return deepReverse(L[1:]) + [L[0]]

print(deepReverse([1,[2,3],4]))
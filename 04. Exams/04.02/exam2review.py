'''
Created on Oct 24, 2017

@author: arusignu
'''

from cs115 import *

#use it/lose it

"""
def ps(L):
    if L == []:
        return [[]]
    lose = ps(L[1:])
    use = map(lambda x: [L[0]]+x, lose)
    return lose + use

# print(ps(['one', 'two']))

def gc(L, n):
    if n == 0:
        return 
    if L == []:
        return float('inf')
    if L[0] > n:
        return gc(L[1:], n)
    lose = gc(L[1:], n)
    use = 1 + gc(L, n-L[0])
    return min(lose, use)

print(gc([1,13,2,5,7], 45))

dict = {key:value}
dict["steve"] = 19
dict[(11,2)] = 12
dict["steve"] = 45
dictionaries can update with new input
"""

def fib(n):
    def fibh(n, memo):
        if n in memo:
            return memo[n]
        if n < 2:
            result = n
        else:
            result = fibh(n-1, memo) + fibh(n-2, memo)
        memo[n] = result
        return result
    return fibh(n, {})

score = {} 
score[(1, 2)] = 'a' 
score[(3, 4)] = 'b' 
score[(2, 1)] = 'c' 

print('a' in score and (1, 2) in score)

def powerset(L):
    if L == []:
        return [[]]
    lose_it = powerset(L[1:])
    use_it = map(lambda subset: [L[0]] + subset, lose_it)
    return lose_it + use_it

print(powerset(['a','b','c']))

lose_it = [[], ['c'],['b'], ['b', 'c']]
print(map(lambda subset: ['a'] + subset, lose_it))

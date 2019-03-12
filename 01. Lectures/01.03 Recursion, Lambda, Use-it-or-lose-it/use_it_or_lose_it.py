'''
Created on Sep 18, 2017

@author: arusignu
'''

from cs115 import map, reduce, filter

def powerset(lst):
    """Returns the power set of the list, that is, the set of all subsets of a list."""
    if lst == []:
        return [[]]
    lose_it = powerset(lst[1:])
    use_it = map(lambda subset: [lst[0]] + subset, lose_it)
    return lose_it + use_it
    
print(powerset(['a','b','c']))

def subset(target, lst):
    #Determines whether or not it is possible to create target sum using the values in the list. Values in the list can be positive, negative, or zero.
    if target == 0:
        return True
    if lst == []:
        return False
    return subset(target-lst[0], lst[1:]) or subset(target, lst[1:])

def subset_with_values(target, lst):
    """Determines whether or not it is possible to create the target 
    sum using values in the list. Values in the list can be positive,
    negative, or zero. The function returns a tuple of  exactly two 
    items. The first is a Boolean that indicates True if the sum is 
    possible and False if it's not. The second element in the tuple 
    is a list of all values that add up to note the target sum."""
    if target == 0:
        return (True, [])
    if lst == []:
        return (False, [])
    use_it = subset_with_values(target -lst[0], lst[1:])
    if use_it[0]:    
        return (True, [lst[0]] + use_it[1])
    return subset_with_values(target,lst[1:])

print(subset_with_values(8, [7,2,2,2,2,]))
print(subset_with_values(12,[1,2,4,9]))

def LCS(S1, S2):
    """Returns the length of the longest common subsequece in strings S1 and S2"""
    if S1 == '' or S2 == '':
        return 0
    if S1[0] == S2[0]:
        return 1 + LCS(S1[1:], S2[1:])
    return max(LCS(S1,S2[1:]),LCS(S1[1:],S2))

def LCS_with_values(S1, S2):
    if S1 == '' or S2 == '':
        return (0, '')
    if S1[0] == S2[0]:
        result = LCS_with_values(S1[1:], S2[1:])
        return (1+result[0], S1[0] + result[1])
    useS1 = LCS_with_values(S1, S2[1:])
    useS2 = LCS_with_values(S1[1:], S2)
    if useS1[0] > useS2[0]:
        return useS1
    return useS2

"""
def coin_row(lst):
    if lst == []:
        return 0
    use_it = lst [0] + coin_row(lst[2:])
    lose_it = coin_row(lst[1:])
    return max(use_it, lose_it)
turn the code above into the code below
"""

def coin_row(lst):
    return 0 if lst == [] else max(lst[0] + coin_row(lst[2:]), coin_row(lst[1:]))

print(coin_row([]))
print(coin_row([5, 1, 2, 10, 6, 2]))
print(coin_row([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))

def coin_row_with_values(lst):
    if lst ==[]:
        return [0, []]
    use_it = coin_row_with_values(lst[2:])
    new_sum = lst[0] + use_it[0]
    lose_it = coin_row_with_values(lst[1:])
    if new_sum > lose_it[0]:
        return [new_sum, [lst[0]] + use_it[1]]
    return lose_it

print(coin_row_with_values([]))
print(coin_row_with_values([5, 1, 2, 10, 6, 2]))
print(coin_row_with_values([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))

def distance(first, second):
    if first == '':
        return len(second)
    if second == '':
        return len()
    if first(0) == second(0):
        return distance(first[1:], second[1:])
    substitution =  distance(first[1:], second[1:])
    deletion = distance(first[1:], second)
    insertion = distance(first, second[1:])
    return 1 + min(substitution, deletion, insertion)
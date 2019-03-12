'''
Created on Feb 20, 2016

@author: Brian Borowski

CS115 - Coin row problem with 'use it or lose it'
'''
def coin_row(lst):
    '''lst represents a row of n coins whose values are some positive integers
    c1, c2, ..., cn, not necessarily distinct.
    Returns the maximum amount of money subject to the constraint that no two
    coins adjacent in the initial row can be picked up.'''
    if lst == []:
        return 0
    return max(lst[0] + coin_row(lst[2:]), coin_row(lst[1:]))

def coin_row_with_values(lst):
    '''lst represents a row of n coins whose values are some positive integers
    c1, c2, ..., cn, not necessarily distinct.
    Returns a list containing
     - the maximum amount of money subject to the constraint that no two
       coins adjacent in the initial row can be picked up, and
     - a list of the coins used to create the maximum sum.'''
    if lst == []:
        return [0, []]
    use_it = coin_row_with_values(lst[2:])
    lose_it = coin_row_with_values(lst[1:])
    new_sum = use_it[0] + lst[0]
    if new_sum > lose_it[0]:
        return [new_sum, [lst[0]] + use_it[1]]
    return lose_it

print(coin_row([]))
print(coin_row_with_values([]))
print(coin_row([5, 1, 2, 10, 6, 2]))
print(coin_row_with_values([5, 1, 2, 10, 6, 2]))
print(coin_row([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))
print(coin_row_with_values([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))

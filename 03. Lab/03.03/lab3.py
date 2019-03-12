'''
Created on 09/21/17
@author:   arusignu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 3
'''

def change(amount, coins):
    """Returns the minimum amount of coins it takes to create the given amount"""
    if amount == 0:
        return 0
    if coins == []:
        return float("inf")
    if coins[0] > amount:
        return change(amount, coins[1:])
    lose_it = change(amount, coins[1:])
    use_it = 1 + change(amount - coins[0],coins)
    return min(use_it,lose_it)

#print(change(4,[2,1,4]))
print(change(131, [1, 5, 10, 20, 50, 100]))
print(change(292, [1, 5, 10, 20, 50, 100]))
print(change(673, [1, 5, 10, 20, 50, 100]))
print(change(724, [1, 5, 10, 20, 50, 100]))
print(change(888, [1, 5, 10, 20, 50, 100]))

def giveChange(amount, coins):
    """Returns the minimum amount of coins it takes to create the given amount"""
    if amount == 0:
        return [0, []]
    if coins == []:
        return [float("inf"),[]]
    if coins[0] > amount:
        return [giveChange(amount, coins[1:])[0],giveChange(amount, coins[1:])[1]]
    lose_it = [giveChange(amount, coins[1:])[0],giveChange(amount, coins[1:])[1]]
    use_it = [1 + giveChange(amount - coins[0],coins)[0],giveChange(amount - coins[0],coins)[1]+[coins[0]]]
    if use_it[0] > lose_it[0]:
        return lose_it
    return use_it
    """return [min(use_it[0],lose_it[0]), [coins[0]]]"""

#print(giveChange(4,[2,1]))
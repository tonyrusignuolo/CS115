'''
Created on Sep 28, 2017

@author: arusignu

I pledge my honor that I have abided by the Stevens Honor Sysstem.
'''

def knapsack(capacity, itemList):
    if capacity == 0 or itemList == []:
        return [0, []]
    if itemList[0][0] > capacity:
        b3 = knapsack(capacity,itemList[1:])
        return [b3[0],b3[1]]
    li = knapsack(capacity,itemList[1:])
    ui = knapsack(capacity - itemList[0][0], itemList[1:])
    lose_it = [li[0], li[1]]
    use_it = [itemList[0][1] + ui[0], [itemList[0]] + ui[1]]
    if use_it[0] > lose_it[0]:
        return use_it
    return lose_it 
    
print(knapsack(6, [[1, 4], [5, 150], [4, 180]]))
print(knapsack(76, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))
print(knapsack(24, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))
print(knapsack(25, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))

"""
def giveChange(amount, coins):
    Returns the minimum amount of coins it takes to create the given amount and the list of coins used to create that amount
    if amount == 0:
        return [0, []]
    if coins == []:
        return [float("inf"),[]]
    if coins[0] > amount:
        return [giveChange(amount, coins[1:])[0],giveChange(amount, coins[1:])[1]]
    li = giveChange(amount, coins[1:])
    ui = giveChange(amount - coins[0],coins)
    lose_it = [li[0],li[1]]
    use_it = [1 + ui[0],ui[1]+[coins[0]]]
    if use_it[0] > lose_it[0]:
        return lose_it
    return use_it
"""
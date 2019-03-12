'''
Created on 10/10/17
@author:   arusignu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5
'''
import turtle, random  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.

def sv_tree(trunk_length, levels):
    """Returns a tree with an input number of branch levels and branch 
    lengths that diminish by half from the level prior""" 
    turtle.left(90)
    
    def svtHelper(distance, angle, count):
        if count < levels:
            turtle.pencolor("brown")
            turtle.forward(distance)
            turtle.left(angle)
            svtHelper(trunk_length/(2**count),angle, count+1)
            turtle.right(2*angle)
            svtHelper(trunk_length/(2**count),angle, count+1)
            turtle.left(angle)
            turtle.backward(distance)
    svtHelper(trunk_length,30,0)

def pretty_tree(trunk_length, levels):
    """Returns a tree with an input number of branch levels and branch 
    lengths that diminish by half from the level prior""" 
    turtle.left(90)
    turtle.pencolor("brown")
    def ptHelper(distance, count):
        a = random.uniform(30,60)
        if count == levels - 1:
            turtle.pencolor("green")
        if count < levels:
            turtle.forward(distance)
            turtle.left(a)
            ptHelper(trunk_length/(2**count), count+1)
            turtle.right(2*a)
            ptHelper(trunk_length/(2**count), count+1)
            turtle.left(a)
            turtle.backward(distance)
            turtle.pencolor("brown")
    ptHelper(trunk_length,0)


def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    def flHelper(n, memo):
        if n in memo:
            return memo[n]
        if n <= 1:
            result = 2 - n
        else:
            result = flHelper(n-1, memo) + flHelper(n-2, memo)
        memo[n] = result
        return result
    return flHelper(n, {})

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        if amount in memo:
            return memo[amount]
        if amount == 0:
            result = 0
        elif coins == ():
            result = float("inf")
        elif coins[0] > amount:
            result = fast_change_helper(amount, coins[1:], memo)
        else:
            lose_it = fast_change_helper(amount, coins[1:], memo)
            use_it = 1 + fast_change_helper(amount - coins[0],coins, memo)
            result = min(use_it,lose_it)
        memo[amount] = result
        return result
    # Call the helper. Note we converted the list to a tuple..
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))
# Should take a few seconds to draw a tree.
pretty_tree(100, 4)
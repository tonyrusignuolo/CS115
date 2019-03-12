'''
Created on Nov 2, 2017

I pledge my honor that I have abided by the Stevens Honor System.

@author: arusignu
'''

def mult(c,n):
    """Uses loops to multiply c by n"""
    result = 0
    for x in range(n):
        result += c
    return result    

# print(mult(1.5,28))

def update(c,n):
    """ update starts with z=0 and runs z = z**2 + c 
        for a total of n times. It returns the final z."""
    z = 0
    for x in range(n):
        z = z**2 + c
    return z
    
# print(update(1,10))

def inMSet(c,n):
    """ inMSet takes in c for the update step of 
    z = z**2+c n, the maximum number of times to 
    run that step Then, it should return False as 
    soon as abs(z) gets larger than 2 True if abs(z) 
    never gets larger than 2 (for n iterations)"""
    z = 0 + 0j
    for x in range(n):
        z = z**2 + c
    return z
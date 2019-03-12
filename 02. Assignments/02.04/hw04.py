'''
Created on Oct 4, 2017

I pledge my honor that I have abided by the Stevens Honor System.

@author: arusignu
'''

def pascal_row(rn):
    """Returns the rnth row of pascal's triangle"""    
    def pr_helper(x):
        """Returns the sum of adjacent values within the list x"""
        if len(x) <= 1:
            return []
        return [x[0]+x[1]] + pr_helper(x[1:])
    if rn == 0:
        return [1]
    if rn == 1:
        return [1, 1]    
    return [1] + pr_helper(pascal_row(rn-1)) + [1]
        
print(pascal_row(0))

def pascal_triangle(rn):
    """Returns a list of pascal's triangle rows to the rnth row""" 
    if rn < 0:
        return []
    return pascal_triangle(rn-1) + [pascal_row(rn)]

print(pascal_triangle(0))
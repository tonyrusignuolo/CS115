'''
Created on Oct 2, 2017

@author: arusignu
'''

def m2(s):
    def helper(s, accum):
        if len(s) == 0:
            return accum
        if s[0] in s[1:]:
            return helper(s[1:], accum)
        return helper(s[1:], accum + s[0])
    return helper(s, '')

print(m2('balloon'))
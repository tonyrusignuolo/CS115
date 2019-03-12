'''
Created on 10/12/17
@author:   arusignu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n % 2 == 1

print(isOdd(4))

#42 base 10 = 101010
#An even number in base 10 will always have a 0 in the right-most position of base 2.
#An odd number in base 10 will always have a 1 in the right-most position of base 2.
#Eliminating the least-significant value of a base 2 number will floor divide the decimal value by 2.
#If N is odd, add a 1 to the end of Y
#If N is even add a 0 to the end of Y

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if isOdd(n) == True:
        return numToBinary(n//2) + '1'
    return numToBinary(n//2) + '0'   
    
print(numToBinary(42))

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    if int(s[-1]) == 1:
        return 1 + 2 * binaryToNum(s[:-1])
    return 2 * binaryToNum(s[:-1])
        
print(binaryToNum('101010'))

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    a = numToBinary(binaryToNum(s)+1)
    if len(a) <= 8:
        return '0' * (8-len(a)) + a
    return '00000000'

print(increment('11111111'))

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n >= 0:
        print(s)
        a = increment(s)
        count(a, n-1)

print(count('11111110',5))

#59 base 10 = 2012 base 3 because 2 * 3^0 + 1 * 3^1 + 0 * 3^2 + 2 * 3^3 = 1 + 3 + 0 + 54 = 59
def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    return numToTernary(n//3) + str(n % 3)

print(numToTernary(0))

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    return int(s[-1]) + 3 * ternaryToNum(s[:-1])

print(ternaryToNum('12211010'))
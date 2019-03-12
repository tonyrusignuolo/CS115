'''
Created on Nov 1, 2017

I pledge my honor that I have abided by the Stevens Honor System.

@author: arusignu
'''

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n % 2 == 1

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if isOdd(n) == True:
        return numToBinary(n//2) + '1'
    return numToBinary(n//2) + '0'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    if int(s[-1]) == 1:
        return 1 + 2 * binaryToNum(s[:-1])
    return 2 * binaryToNum(s[:-1])
        
def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    a = numToBinary(binaryToNum(s)+1)
    if len(a) <= 8:
        return '0' * (8-len(a)) + a
    return '00000000'

def numToBaseB(N,B):
    """Returns a string of the number N with a base of B"""
    if N == 0:
        return ''
    return numToBaseB(N//B,B) + str(N % B)

def baseBToNum(S,B):
    """Returns a decimal number of the number with a base of 
    B represented in the string S"""
    if S == '':
        return 0
    return int(S[-1]) + B * baseBToNum(S[:-1],B)

def padNum(n,cbs):
    """Converts an integer into a binary string with padded zeros"""
    a = numToBinary(n)
    if len(a) <= cbs:
        return '0' * (cbs-len(a)) + a

def myTcToNum(S):
    i = baseBToNum(S[1:],2)
    if S[0] == '0':
        return i
    else:
        return -128 + i

def TcToNum(S):
    """Returns the integer value of the twos compliment S"""
    if S[0] == '0':
        return baseBToNum(S,2) 
    else:
        def TTNHelper(S):
            if S == '':
                return ''
            if S[0] == '0':
                return '1' + TTNHelper(S[1:])
            if S[0] == '1':
                return '0' + TTNHelper(S[1:])
        return -baseBToNum(increment(TTNHelper(S)),2)

#print(TcToNum('10000000'))    
#print(myTcToNum('01000000'))

def NumToTc(N):
    """Returns the twos compliment of the integer N"""
    if N > 127 or N < -128:
        return 'Error'
    if N >= 0:
        return padNum(N,8)
    else:
        def NTTHelper(S):
            if S == '':
                return ''
            if S[0] == '0':
                return '1' + NTTHelper(S[1:])
            if S[0] == '1':
                return '0' + NTTHelper(S[1:])
        return increment(NTTHelper((padNum(-N,8))))
    
print(NumToTc(1))
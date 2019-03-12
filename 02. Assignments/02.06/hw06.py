'''
Created on 10/18/17
@author:   arusignu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''

from cs115 import *

# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

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

def count_run(S, n, mrl):
    """Counts the number of similar string items at the beginning of a string"""
    if S == '':
        return 0
    if mrl == 0:
        return 0
    if int(S[0]) == n:
        return 1 + count_run(S[1:], n, mrl-1)
    return 0

#print(count_run('01'*32, 0, MAX_RUN_LENGTH))

def padNum(n,cbs):
    """Converts an integer into a binary string with padded zeros"""
    a = numToBinary(n)
    if len(a) <= cbs:
        return '0' * (cbs-len(a)) + a
    
#print(padNum(7, COMPRESSED_BLOCK_SIZE))

def compress(S):
    """Compresses a 64 bit string into 5 bit blocks"""
    def cH(S,n):
        if S == '':
            return ['',0]
        a = count_run(S,n,MAX_RUN_LENGTH)
        return [padNum(a,COMPRESSED_BLOCK_SIZE), a]
    if S == '':
        return ''
    else:
        b = count_run(S,0,MAX_RUN_LENGTH)
        c = cH(S[b:],1)
        return padNum(b,COMPRESSED_BLOCK_SIZE) + c[0] + compress(S[(b+c[1]):])
    return

#print(compress('10'*32))
#print('0000000001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001')
print(len(compress('10'*32)))
"""325 bits is the max length. Assuming every bit of the uncompressed code is 
different and it starts with one you'll have five initial zeros for the lack of a 
zero at the beginning of the uncompressed and 5 bits for every different value 
after that. 5 + 5 * 64 = 325"""
  
def uncompress(C):
    if C == '':
        return ''
    return '0' * binaryToNum(C[0:COMPRESSED_BLOCK_SIZE]) + '1' * binaryToNum(C[COMPRESSED_BLOCK_SIZE:(2*COMPRESSED_BLOCK_SIZE)]) + uncompress(C[(2*COMPRESSED_BLOCK_SIZE):])

def compression(S):
    return len(compress(S))/len(S)

penguin = "00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"
smile = "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8
five = "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"

"""Increasing the cbs in the largest bit case mentioned 
above would only increase that value by the delta of the times 64. 
Decreasing cbs would increase the compressed bit length in the case 
of an uncompressed string with 64 0s""" 

print(compress(penguin))
# 00011000100010100100001000010000100001000001100110000010100000010001000010000001000100000100010
print(compression(penguin))
# 1.484375
print(compress(smile))
# 0100100010000100001000010000100001000010011010000100100000010010000001000100011001001
print(compression(smile))
# 1.328125
print(compress(five))
# 00000010010011100001001110000100111001110100000001001110100000001
print(compression(five))
# 1.015625
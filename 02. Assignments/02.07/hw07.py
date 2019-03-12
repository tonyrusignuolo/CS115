'''
Created on 10/25/17
@author:   arusignu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 7
'''

FullAdder = { ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }

def numToBaseB(N,B):
    """Returns a string of the number N with a base of B"""
    if N == 0:
        return ''
    return numToBaseB(N//B,B) + str(N % B)

#print(numToBaseB(0,4))

def baseBToNum(S,B):
    """Returns a decimal number of the number with a base of 
    B represented in the string S"""
    if S == '':
        return 0
    return int(S[-1]) + B * baseBToNum(S[:-1],B)

#print(baseBToNum('',10))

def baseToBase(B1,B2,SinB1):
    """Converts a number of base B1 represented as 
    a string to another string represented number 
    of base B2"""
    return numToBaseB(baseBToNum(SinB1,B1),B2)

#print(baseToBase(3,5,'11'))

def add(S,T):
    """Adds two binary strings using integer functions written above"""
    return numToBaseB((baseBToNum(S,2)+baseBToNum(T,2)),2)

#print(add('110','011'))

def addB(S,T):
    """Adds two binary strings without using integers, 
    leading 0s, or functions written above"""
    def addBH(S,T,c):
        if S == '' and T == '' and c == '1':
            return c
        if S == '' and T == '':
            return ''
        if S == '':
            s,c = FullAdder[('0',T[-1],c)] 
        elif T == '':
            s,c = FullAdder[(S[-1],'0',c)]
        else:
            s,c = FullAdder[(S[-1],T[-1],c)]
        return addBH(S[:-1],T[:-1],c) + s
    def trim(str):
        if str[0] != '0':
            return str
        return trim(str[1:])
    return trim(addBH(S,T,'0'))

print(addB("000", "000100"))
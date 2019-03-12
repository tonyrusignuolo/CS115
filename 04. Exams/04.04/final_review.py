'''
Created on Dec 7, 2017

@author: arusignu
'''

def LCSuioli(S1, S2):
    if S1 == '' or S2 == '':
        return 0
    if S1[0] == S2[0]:
        return 1 + LCS(S1[1:],S2[1:])
    return max(LCS(S1[1:],S2), LCS(S1,S2[1:]))

def LCSuioli_wv(S1, S2):
    if S1 == '' or S2 == '':
        return [0, '']
    if S1[0] == S2[0]:
        result = LCSuioli_wv(S1[1:], S2[1:])
        return [1 + result[0], S1[0] + result[1]]
    useS1 = LCSuioli_wv(S1, S2[1:])
    useS2 = LCSuioli_wv(S1[1:], S2)
    if useS1[0] > useS2[0]:
        return useS1
    return useS2

r = range(5, -1, -2)
print(0//2) 
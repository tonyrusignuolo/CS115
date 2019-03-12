'''
Created on 09/18/17
@author:   arusignu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - HW 2
'''
import sys
from cs115 import map, reduce, filter

#import * imports everything instead of explicitly stated things


# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

'''
Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']
'''

# Implement your functions here.

Dictionary = ['902', '820', '888', '270', '999', '123', '456', '789', '203', '884', '423', '723', '210', '98546']
bonglePoints = \
    [ ['0', 1.2], ['1', 3.3], ['2', 3.1], ['3', 2.5], ['4', 1.0],
     ['5', 4.9], ['6', 2.8], ['7', 4.2], ['8', 1.1], ['9', 8.1] ]

"""
def bestCode(numbers):
    contenders = pointsList(numbers)
    def betterCode(x,y):
        if x[1] > y[1]:
            return x
        return y
    return reduce(lambda x, y: (if x[1] > y[1] else y,contenders))
    return reduce(betterCode, contenders)
"""

"""
print(pointsList(['9', '8' '7', '3', '2', '1', '0', '5', '4', '6', '8'])
"""

def remove(number, numbers):
    if numbers == []:
        return []
    if number == numbers [0]:
        return numbers [1:]
    else:
        return [numbers[0]] + remove(number, numbers[1:])

print(remove('9', ['0', '9', '8']))

def is_code_possible(code, numbers):
    if code == '':
        return True
    if code[0] in numbers:
        return is_code_possible(code[1:], remove(code[0], numbers))
    else:
        return False    

print(is_code_possible('908', ['0', '9', '8']))
print(is_code_possible('910', ['0', '9', '8']))
print(is_code_possible('902', Dictionary))

def list_of_codes_created(dictionary, number):
    return filter(lambda code: is_code_possible(code, number),Dictionary)

print(list_of_codes_created(Dictionary, ['9', '8', '5', '4', '6']))

def codePoints(code, pointsList):
    if code =="":
        return 1
    return numberPoints(code[0], pointsList) * codePoints(code[1:], pointsList)

def pointsList(numbers):
    code = list_of_codes_created(Dictionary, numbers)
    return map(lambda code: [code, codePoints(code, bonglePoints)], code)
# ['456', '98546'] ->
[['456', 12], ['908', 13]]

def numberPoints(number, pointsList):
    '''Returns the points for a given number.'''
    if pointsList ==[]:
        return 0.0
    first = pointsList[0]
    if first[0] == number:
        return first[1]
    return numberPoints(number, pointsList[1:])

print(numberPoints('9', bonglePoints))
#should return 8.1


#code ='876'
# ['0', '9', '8']
'''
Created on 09/20/17
@author:   arusignu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
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

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scorelist):
    if scorelist==[]:
        return 0.0
    if scorelist[0][0] == letter:
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    if S == '':
        return 0.0
    return letterScore(S[0],scorelist) + wordScore(S[1:],scorelist)

def remove(letter, letters):
    if letters == []:
        return []
    if letter == letters[0]:
        return letters[1:]
    return [letters[0]]+remove(letter, letters[1:])

print(remove('b',['b','b','b','l','r']))

def is_word_possible(word, rack):
    if word =='':
        return True
    if word[0] in rack:
        return is_word_possible(word[1:],remove(word[0], rack))
    return False

def list_of_possible_words(dictionary, rack):
    return filter(lambda word: is_word_possible(word, rack), dictionary)

def scoreList(rack):
    lopw = list_of_possible_words(Dictionary, rack)
    return map(lambda word: [word, wordScore(word,scrabbleScores)],lopw)

def bestWord(rack):
    contenders = scoreList(rack)
    if contenders == []:
        return ['',0]
    def betterWord(x,y):
        if x[1] > y[1]:
            return x
        return y
    return reduce(betterWord, contenders)

print(bestWord(['g', 'y', 'e']))
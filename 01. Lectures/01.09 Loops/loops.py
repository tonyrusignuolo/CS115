'''
Created on Oct 31, 2017

@author: arusignu
'''

def leppard (input_string):
    output_string = ''
    for symbol in input_string:
        if symbol == 'o':
            output_string = output_string + 'ooo'
        else:
            output_string = output_string + symbol
    return output_string

vowels = ['a','e','i','o','u']

def spamify(word):
    for i in range(len(word)):
        if word[i] not in vowels:
            return word[0:i] + 'spam' + word[i+1:]
    return word


def mymapSqr(L):
    L2 = []
    for i in range(len(L)):
        L2 += [L[i]**2]
    return L2

def bbmapSqr(L):
    result = []
    for x in L:
        result.append(x*x)
    return result

#print(mymapSqr([1,2,3,4]))
#print(bbmapSqr([1,2,3,4]))

def find_max(lst):
    if lst == []:
        return None
    max_val = lst[0]
    for x in lst:
        if max_val < x:
            max_val = x
    return max_val

#print(find_max([1, 32, 45, 32]))

def find_min_max(lst):
    if lst == []:
        return None
    min_val = max_val = lst[0]    
    for x in lst:
        if max_val < x:
            max_val = x
        elif min_val > x:
            min_val = x
    return (min_val, max_val)

#print(find_min_max([1,2,3,45,6,9,-1]))

def sequential_search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

#print(sequential_search([0,1,5,6],5))

def shallow_copy(L):
    new_list = []
    for x in L:
        new_list.append(x)
    return new_list

"""
L = [1,2,3]
M = shallow_copy(L)
M[2] = 33
print(L)
print(M)

S = [[1,2],[3,4],[5,6]]
T = shallow_copy(S)
T[2][1] = 66
print(S)
print(T)
T[2] = [55,66]
print(S)
print(T)
"""

"""appending the second list two pointer levels deep 
will change the original list. Appending the second list
one pointer level deep will will not append the original
list"""

def deep_copy(L):
    new_list = []
    for x in L:
        if isinstance(x,list):
            new_list.append(deep_copy(x))
        else:
            new_list.append(x)
    return new_list

S = [[1,2],[3,4],[5,6]]
T = deep_copy(S)
T[2][0] = 7
print(S)
print(T)

def create_board(r,c):
    board = []
    for _ in range(r):
        row = []
        for _ in range(c):
            row.append(' ')
        board.append(row)
    return board

# print(create_board(3,3))

def create_board_comp(r,c):
    return [[' ' for _ in range(c)] for _ in range(r)]

"""
board = create_board(3,3)
print(board)
board = create_board_comp(3,3)
board[0][0] = 'X'
board[2][2] = 'O'
print(board)
"""

def display_board(board):
    num_rows = len(board)
    for row in range(num_rows):
        num_cols = len(board[row])
        for col in range(num_cols):
            print(' ' + board[row][col] + ' ', end= '')
            if col < num_cols - 1:
                print('/', end='')
        print()
        if row < num_rows - 1:
            print('-' * (num_cols * 4 - 1))
        
board = create_board(3,3)
print(board)
board = create_board_comp(3,3)
board[0][0] = 'X'
board[2][2] = 'O'
print(board)
display_board(board)

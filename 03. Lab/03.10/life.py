#
# life.py - Game of Life lab
#
# Name: arusignu
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#

import random, sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

# print(createOneRow(5))

def createBoard(width,height):
    """Retuns a 2D list of height rows and width columns."""
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

# print(createBoard(3, 2))

def printBoard(A):
    """This function prints the 2s list-of-lists A without spaces
    (using sys.stdout.write)"""
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')

# A = createBoard(5, 3)
# printBoard(A)

def diagonalize(width,height):
    """Creates an empty board and then modifies it so that it has
    a diagonal strip of 'on' cells."""
    A = createBoard(width,height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

# A = diagonalize(7, 6)
# print(A)
# print(printBoard(A))

def innerCells(w,h):
    """Returns a 2d array of all live cells except for a one cell
    wide border of empty cells"""
    A = createBoard(w,h)
    for row in range(1,h-1):
        for col in range(1,w-1):
            A[row][col] = 1
    return A

# A = innerCells(7, 6)
# print(A)
# print(printBoard(A))

def randomCells(w,h):
    """Returns an array of randomly assigned 1s and 0s except for
    the outer edge"""
    A = createBoard(w,h)
    for row in range(1,h-1):
        for col in range(1,w-1):
            A[row][col] = random.choice([0,1])
    return A

# A = randomCells(4, 4)
# print(A)
# print(printBoard(A))

def copy(A):
    """Retuns a deep copy of A"""
    copy = createBoard(len(A), len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            copy[i][j] = A[i][j]
    return copy

"""
oldA = randomCells(4,4)
printBoard(oldA)
print('')
newA = copy(oldA)
printBoard(newA)
print('')
oldA[0][0] = 1
printBoard(oldA)
print('')
printBoard(newA)
"""

def innerReverse(A):
    """Returns a reversed inner board of A."""
    reverse = copy(A)
    for i in range(1,len(A)-1):
        for j in range(1,len(A[0])-1):
            if A[i][j] == 0:
                reverse[i][j] = 1
            else:
                reverse[i][j] = 0
    return reverse

"""
"A = randomCells(5, 5)
printBoard(A)
print('')
A2 = innerReverse(A)
printBoard(A2)
print('')
"""

def countNeighbors(row,col,A):
    count = -A[row-1][col-1]
    for i in range(row-2,row+1):
        for j in range(col-2, col+1):
            if A[i][j] == 1:
                count += 1
    return count

# print(countNeighbors(2,2,A))

def next_life_generation(A):
    """Makes a copy of A and then advanced one generation of
    Conway's Game of Life within the inner cells of that copy.
    The outer edge always stays 0."""
    nl = copy(A)
    for i in range(1,len(A)-1):
        for j in range(1, len(A[0])-1):
            a = countNeighbors(i+1, j+1, A) 
            if A[i][j] == 1 and (a < 2 or a > 3):
                nl[i][j] = 0
            elif A[i][j] == 0 and a == 3:
                nl[i][j] = 1
    return nl

""""
A = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
printBoard(A)
print('')
A2 = next_life_generation(A)
printBoard(A2)
print('')
A3 = next_life_generation(A2)
printBoard(A3)
"""
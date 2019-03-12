'''
Created on Oct 5, 2017

@author: arusignu
'''

import turtle

def square_spiral(walls):
    def square_spiral_helper(distance, initial, count):
        #distance is the distance of the current wall
        #initial is the length of the first wall on the inner part of the spiral
        #count is the number of walls
        if count == walls:
            turtle.done()
        else:
            turtle.left(45)
            turtle.forward(distance)
            square_spiral_helper(distance + initial * (count % 2), initial, count + 1)
    
    square_spiral_helper(20, 5, 0)

square_spiral(30)

print(7%2)
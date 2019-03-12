"""
Created on Jan 26, 2016
Last modified on Jan 26, 2017
@author: Brian Borowski

CS115 - Temperature Conversion
"""

"""
Put functions at the top of the program.
"""

def fahrenheit(celsius):
    """Returns the input Celsius degrees in Fahrenheit."""
    return 9 / 5 * celsius + 32

def celsius(fahrenheit):
    """Returns the input Fahrenheit degrees in Celsius."""
    return 5 / 9 * (fahrenheit - 32)

"""
Call the functions below the function definitions.
"""
c = float(input('Enter degrees in Celsius: '))
f = fahrenheit(c)
# You can print multiple items in one statement. If you put a comma after each
# item, it prints a space and then goes on to print the next item.
print(c, 'C =', f, 'F')
# You can print this way too, but allowing exactly two decimal places.
print('%.2f C = %.2f F' % (c, f))

f = float(input('Enter degrees in Fahrenheit: '))
c = celsius(f)
print(f, 'F =', c, 'C')
print('%.2f F = %.2f C' % (f, c))

"""
Try composition of functions.
Converting a Fahrenheit temperature to Celsius and back to Fahrenheit should
give you the original Fahrenheit temperature.
"""

print()  # print by itself prints a new line.
f = float(input('Enter degrees in Fahrenheit: '))

# Use assert to check the returned value is equal to the expected value.
assert fahrenheit(celsius(f)) == f
# No output should be produced, unless the assertion fails, which means you
# have an error (either in your code or your expectation).

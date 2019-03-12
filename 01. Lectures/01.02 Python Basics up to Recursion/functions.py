from cs115 import map, reduce, filter
import math

def mult(x, y): 
    """Returns the product of x and y""" 
    return x * y

def add(x, y):
    """Returns the sum of x and y."""
    return x + y

def sum(L):
    """Returns the sum of a list, L."""
    return reduce(add, L)

def mean(L):
    """Returns the average value of a list, L."""
    return sum(L)/len(L)

def factorial(n):
    """Returns the factorial of a given number, n."""
    if n==0:
        return 1
    return n*factorial(n-1)
    
def divides(n):
    def div(k):
        return n % k == 0
    return div

"""
def prime(n):
    #Returns whether the integer n is prime or not.
    return sum(map(divides(n),range(1,n+1))) == 2
"""

def tower(n):
    """Computes 2^(2^(2...)) with n twos, using recursion."""
    if n==0:
        return 1
    return 2 ** tower(n-1)
 
def tower_reduce(n):
    def power(x, y):
        return y ** x
    if n==0:
        return 1
    return reduce(power, [2] * n)
 
def length(lst):
    """Returns the length of the list."""
    if lst == []:
        return 0
    return length(lst[1:])
    
def reverse(lst):
    """Takes as input a list of elements and returns the list in reverse order."""
    if lst == []:
        return []
    return reverse(lst[1:]) + [lst[0]]

def member(x, lst):
    """Returns true if x is contained in the list and false otherwise."""
    if lst ==[]:
        return False
    if x == lst[0]:
        return True
    return member(x, lst[1:])

def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y - 1)

def power_tail(x,y):
    """Returns the exponent x^y."""
    def power_tail_helper(x,y,accum):
        if y == 0:
            return accum
        return power_tail_helper(x, y - 1, x * accum)
    return power_tail_helper(x,y,1)

def mystery(n):
    return m_help(n,0)

def m_help(n,r):
    """Returns the mirror of most intergers, n."""
    if n == 0:
        return r
    return m_help(n // 10, r * 10 + n % 10)

def my_map(f, lst):
    """"""
    if lst ==[]:
        return []
    return [f(lst(0))] + my_map(f, lst[1:])

def my_reduce(f, lst):
    def my_reduce_helper(f, lst, accum):
        if lst==[]:
            return accum
        return my_reduce_helper(f, lst[1:], f(lst[0], accum))
    if lst ==[]:
        raise TypeError('my_reduce() of empty sequence with no initial value')
    return my_reduce_helper(f, lst[1:], lst[0])

def prime(n):
    """Returns whether or not an integer is prime."""
    possible_divisors = range(2, int(math.sqrt(n)+1))
    divisors = filter(lambda x: n % x == 0, possible_divisors)
    return len(divisors) == 0

print(lambda)

def primes(n):
    """Returns a list of primes in the range [2,n] computed via the sieve of Erotosthemes."""
    def sieve(lst):
        if lst == []:
            return []
        return [lst[0]]+ sieve(filter(lambda x: x % lst[0] != 0, lst[1:]))
    return sieve(range(2,n+1))

def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
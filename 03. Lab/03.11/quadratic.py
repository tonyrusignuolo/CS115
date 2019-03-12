'''
Created on Nov 16, 2017

@author: arusignu

I pledge my honor that I have abided by the Stevens Honor System.
'''

class QuadraticEquation(object):
    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
        
    @property
    #getter
    def a(self):
        return self.__a
    
    @property
    #getter
    def b(self):
        return self.__b
    
    @property
    #getter
    def c(self):
        return self.__c
    
    #method
    def discriminant(self):
        return (self.__b ** 2) - 4 * self.__a * self.__c 
    
    #method
    def root1(self):
        d = self.discriminant()
        if d < 0:
            return None
        else:
            return (self.__b * -1 + (d ** .5)) / (2 * self.__a) 
    
    #method
    def root2(self):
        d = self.discriminant()
        if d < 0:
            return None
        else:
            return (self.__b * -1 - (d ** .5)) / (2 * self.__a)
        
    def __str__(self):
        s1 = ''
        a1 = str(abs(self.__a))
        x1 = 'x^2 '
        s2 = '+ '
        b2 = str(abs(self.__b))
        x2 = 'x '
        s3 = '+ '
        c3 = str(abs(self.__c))
        x3 = ' '
        end = '= 0'
        
        if self.__a < 0:
            s1 = '-'
        if self.__b < 0:
            s2 = '- '
        if self.__c < 0:
            s3 = '- '
        if self.__b == 0:
            s2 = ''
            b2 = ''
            x2 = ''
        if self.__c == 0:
            s3 = ''
            c3 = ''
            x3 = ''
        if abs(self.__a) == 1:
            a1 = ''
        if abs(self.__b) == 1:
            b2 = ''
        return s1 + a1 + x1 + s2 + b2 + x2 + s3 + c3 + x3 + end
     
q1 = QuadraticEquation(1.0,2.0,0.0)
print(q1)         

if __name__ == '__main__':
    pass
    
"""    
@poperties
    @getters
    @setters
@methods
@operations +-><>=<=!==
"""
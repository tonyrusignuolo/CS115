'''
Created on 11/9/2017
@author:   arusignu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 11 - Date class
'''

DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self): 
        '''Returns a new object with the same month, day, year 
           as the calling object (self).''' 
        dnew = Date(self.month, self.day, self.year) 
        return dnew
    
    def equals(self, d2): 
        '''Decides if self and d2 represent the same calendar date, 
            whether or not they are the in the same place in memory.''' 
        return self.year == d2.year and self.month == d2.month and \
            self.day == d2.day
            
    def tomorrow(self):
        '''Changes the calling object so that it represents one 
        calendar day after the date it originally represented.'''
        DIM = (0,31,28,31,30,31,30,31,31,30,31,30,31)
        if self.isLeapYear() and self.month == 2: #02/29/ly
            if self.day == 29:
                self.month = 3
                self.day = 1
            else: self.day += 1
        elif self.day == DIM[self.month]:
            if self.month == 12:
                self.year += 1
                self.month = 1
                self.day = 1
            else:
                self.month += 1
                self.day = 1
        else:
            self.day += 1         

    def yesterday(self):
        '''Changes the calling object so that it represents one 
        calendar day after the date it originally represented.'''
        DIM = (0,31,28,31,30,31,30,31,31,30,31,30,31)
        if self.isLeapYear() and self.month == 3 and self.day == 1: #02/29/ly
            self.month = 2
            self.day = 29
        elif self.day == 1:
            if self.month == 1:
                self.year += -1
                self.month = 12
                self.day = 31
            else:
                self.month += -1
                self.day = DIM[self.month]
        else:
            self.day += -1
            
    def addNDays(self, N):
        '''Changes the calling object so that it represents N 
        calendar day(s) after the date it originally represented.'''
        print(self)
        for x in range(N):
            self.tomorrow()
            print(self)
        return
    
    def subNDays(self, N):
        '''Changes the calling object so that it represents one 
        calendar day after the date it originally represented.'''
        print(self)
        for x in range(N):
            self.yesterday()
            print(self)
        return

    def isBefore(self, d2):
        '''Determines whether the calling object is a calendar date
        prior to d2.'''
        if self.year < d2.year or (self.year == d2.year and self.month < d2.month) or (self.year == d2.year and self.month == d2.month and self.day < d2.day):
            return True
        else:
            return False
        
             
    def isAfter(self, d2):
        '''Determines whether the calling object is a calendar date
        prior to d2.'''
        try:     
            if self.year > d2.year or (self.year == d2.year \
            and self.month > d2.month) or (self.year == d2.year \
            and self.month == d2.month and self.day > d2.day):
                return True
            else:
                return False    
        except TypeError as error:
            print('Error')

    def diff(self, d2):
        '''Return the amount of days between the calling object and 
        d2.'''
        self_copy = Date(self.month, self.day, self.year)
        d2_copy = Date(d2.month, d2.day, d2.year)         
        if self_copy == d2_copy:
            return 0
        elif self_copy.isBefore(d2_copy):
            i = 0
            while self_copy.isBefore(d2_copy):
                self_copy.tomorrow()
                i += -1
            return i
        else:
            i = 0
            while self_copy.isAfter(d2_copy):
                self_copy.yesterday()
                i += 1
            return i
                 
    def dow(self):
        '''Returns the day of the week.'''
        i = self.diff(Date(11,7,2011)) % 7
        if i == 0:
            return 'Monday'
        elif i == 1:
            return 'Tuesday'
        elif i == 2:
            return 'Wednesday'
        elif i == 3:
            return 'Thursday'
        elif i == 4:
            return 'Friday'
        elif i == 5:
            return 'Saturday'
        elif i == 6:
            return 'Sunday' 
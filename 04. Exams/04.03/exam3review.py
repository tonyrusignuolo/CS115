'''
Created on Nov 29, 2017

@author: arusignu
'''

class MotorBoat(object):
    def __init__(self, overall_length, waterline_length, weight, horsepower):
        self.__overall_length = overall_length
        self.__waterline_length = waterline_length
        self.__weight = weight
        self.__horsepower = horsepower
        
    @property
    def horsepower(self):
        return self.__horsepower
    
    @horsepower.setter
    def horsepower(self, horsepower):
        self.__horsepower = horsepower
        
    def get_max_speed(self):
        return 225 * (self.__horsepower / self.__weight) ** .5
    
    def __str__(self):
        return '%s:\n  Overall length: %.1f meters\n' \
               '  Waterline length: %.1f meters\n' \
               '  Weight: %d pounds\n  Horsepower: %d\n' \
               '  Max speed: %.1f mph' % \
            (self.__class__.__name__, self.__overall_length, \
             self.__waterline_length, self.__weight, \
             self.__horsepower, self.get_max_speed())
            
d = MotorBoat(5,10,15,20)
print(d)

class MotorSailor(MotorBoat):
    def __init__(self, overall_length, waterline_length, weight, horsepower, sail_dimension):
        """
        self.__overall_length = overall_length
        self.__waterline_length = waterline_length
        self.__weight = weight
        self.__horsepower = horsepower
        """
        super.__init__(overall_length, waterline_length, weight, horsepower)
        if type(sail_dimension) != float:
            raise TypeError('Sail dimensions must be a float')
        if sail_dimension < 0:
            raise ValueError('Sail dimensions cannot be negative')
        self.__sail_dimension = sail_dimension

    def get_max_speed(self):
        return ((self.__sail_dimension ** 2) / 3.5) + super().get_max_speed()
    
class Employee(object):
    def __init__(self, first_name, last_name, title, hours_per_week, hourly_rate):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__title = title
        self.__hours_per_week = hours_per_week
        self.__hourly_rate = hourly_rate
        
    @property
    def hourly_rate(self):
        return self.__hourly_rate
    
    @hourly_rate.setter
    def hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate
        
    def get_total_compensation(self):
        return 50 * self.__hourly_rate * self.__hours_per_week

x = 4
y = 1
print(y / x)
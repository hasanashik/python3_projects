# -*- coding: utf-8 -*-
"""
Created on Sat May  8 00:46:02 2021

@author: Hasan-Uz-Zaman Ashik
"""


class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop    # stop defines the range (exclusive upper bound) in which we search for the primes
        self.pre_value = 2 
    def __next__(self):
    #ashik code start
        #print('self.stop = ',self.stop, 'self.pre_value = ', self.pre_value)

        for n in range(self.pre_value, self.stop):
            #print('self.stop = ',self.stop, 'self.pre_value = ', self.pre_value)
            if self.pre_value >= self.stop-1:
                #print('Caught in if')
                raise StopIteration()
            #print('n = ',n)
            if n == 2:
                self.pre_value = n+1
                return n
            for x in range(2,n):
                #print('x = ',x)
                if n%x == 0:
                    self.pre_value = n+1
                    break
            else:
                #print('prime number = ',n)
                self.pre_value = n+1
                return n

        raise StopIteration()
    def __iter__(self):
        return self


for i in PrimeGenerator(100000):
    print('i = ',i)





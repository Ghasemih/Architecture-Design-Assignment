## @file   Data.py
#  @author Hamid Ghasemi 400028420
#  @brief  Provides multiples functions and a class
#  @date   08/02/2018

from SeqServices import *
from Exceptions import *
from CurveADT import *

## @brief Making class Data
class Data():
    global MAX_SIZE
    MAX_SIZE = 10

    ## @brief Data_init is a funtion we define our objects in the class
    #  @details It makes two empty sequences S and Z  
    def init(self):

        self.S = [ ]
        self.Z = [ ]

    ## @brief Data_add is a funtion that add a value to sequence S and Z
    #  @details First checks if the sequence has reached the max size
    #  or not then checks if s and z are the bigger values than the last
    #  the last value of S and Z. If the condition meets then it adds the value
    #  s and z.
    #  @param s is a sequence
    #  @param z is a sequence
    def add(self, s, z):
        if ( len(self.S) == MAX_SIZE ):
            raise Full("There is no space")
        elif ( self.Z != []):
            if (z <= self.Z[len(self.Z)-1]):
                raise IndepVarNotAscending("It's not ascended")
        
        self.S = self.S + s
        self.Z = self.Z + z

    ## @brief Data_getC is a funtion
    #  @details It returns a value from the sequence by using an index i
    #  @param i is a value that uses as an index of sequence S and Z
    #  @return value from the sequence
    def getC(self, i):
        if ( i < 0 or i >= len(self.S)):
            raise InvalidIndex("i is out of range")
            
        return self.S[i]

    ## @brief Data_eval is a funtion
    #  @details It uses index and interpLin functions to return a value
    #  @param x is a input value
    #  @param z is a input value
    #  @return a value by using interpLin function
    def eval(self, x, z):
        if (isInBounds(self.Z, z) == False):
            raise OutOfDomain("z is out of range")

        j = index(self.Z,z)
        d = interpLin(self.Z[j], self.S[j].eval(x), self.Z[j+1], self.S[j+1].eval(x), z)               
        return d

    ## @brief Data_slice is a funtion
    #  @details It checks if i is within index of sequence Z then uses x and i values
    #  and returns CurveT based on Z,Y, and i
    #  @param x is a input value
    #  @param i is a input value
    #  @return CurveT
    def slice(self,x,i):
        while(0 <= i <= len(self.Z)-1):
            Y = self.S[i].eval(x)
            return CurveT(self.Z, Y, i)
        




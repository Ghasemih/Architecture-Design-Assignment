## @file   CurveADT.py
#  @author Hamid Ghasemi 400028420
#  @brief  Provides function and a class
#  @date   08/02/2018

from SeqServices import *
from Exceptions import *

## @brief interp is a local function 
#  @details Gets all the inputs and determine y as interpLin if o = 1, interpQuad when 
#  o = 2 
#  @param X is the first input sequence
#  @param Y is the second input sequence
#  @param o is the order of the function that user inputs
#  @param v is the input value
#  @return interpLin, interpQuad or False

def interp(X, Y, o, v):
    i = index(X, v)
    if ( o == 1 ) :
        return interpLin(X[i], Y[i], X[i+1], Y[i+1], v)
    elif ( o == 2 ):
        return interpQuad(X[i-1], Y[i-1], X[i], Y[i], X[i+1], Y[i+1], v)
    else:
        return False

## @brief Making class curveT
class CurveT():
    global MAX_ORDER, DX

    MAX_ORDER = 2
    DX = 0.001

    ## @brief CurveT constructor
    #  @details It finds the maximum, minimum, order of function, and 
    #  at the end it makes function f by using interp function
    #  @param X is a sequence that user inputs
    #  @param Y is a sequence that user inputs
    #  @param i is value that user inputs
    def __init__(self, X, Y, i):
        if (isAscending(X) == False):
            raise IndepVarNotAscending("It's not ascended")
        elif (len(X) != len(Y)) :
            raise SeqSizeMismatch("X and Y dont have same length")
        elif (i not in range(1,MAX_ORDER +1)):
            raise InvalidInterpOrder("i does not follow the condition")   
    
        self.minx = X[0]
        self.maxx = X[-1]
        self.o    = i
        self.f = lambda v : interp(X,Y,self.o,v)

    ## @brief minD is a funtion
    #  @details It returns minimum value of sequence X that has been 
    #  defined in the constructor
    #  @return minimum 
    def minD(self):
        return self.minx

    ## @brief maxD is a funtion
    #  @details It returns maximum value of sequence X that has been  
    #  defined in the constructor
    #  @return maximum
    def maxD(self):
        return self.maxx
    
    ## @brief order is a funtion
    #  @details It returns the order that user has inputed 
    #  @return maximum
    def order(self):
        return self.o 

    ## @brief eval is a funtion
    #  @details It returns function f based on x   
    #  @param x is a value user inputs
    #  @return function f   
    def eval(self, x):
        if ( self.minx > x or x > self.maxx):
            raise OutOFDomain("x is not in the range")
        return self.f(x)

    ## @brief dfdx is a funtion
    #  @details It returns a value by using the equation (f(x+DX)-f(x))/DX    
    #  @param x is a value user inputs
    #  @return function f 
    def dfdx(self, x):
        if ( self.minx > x or x > self.maxx):
            raise OutOFDomain("x is not in the range")
        d = (f(x+DX)-f(x))/DX
        return d

    ## @brief d2fdx2 is a funtion
    #  @details It returns a value by using the equation (f(x+2*DX)-2*f(x+DX)+f(x))/(DX**2)   
    #  @param x is a value user inputs
    #  @return function f 
    def d2fdx2(self, x):
        if ( self.minx > x or x > self.maxx ):
            raise OutOFDomain("x is not in the range")
        d = (f(x+2*DX)-2*f(x+DX)+f(x))/(DX**2)
        return d

    

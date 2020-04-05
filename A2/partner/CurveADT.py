## @file CurveADT.py
# @title CurveT
# @author Somar Aani
# @date 07/02/2018

from SeqServices import *
from Exceptions import *

## @brief Class representing a curve
class CurveT:  
    
    MAX_ORDER = 2
    DX = 0.001
    
    ## @brief CurveT constructor
    # @details constructs the curve using the data provided
    # @param Real[]: X list of X values for the curve
    # @param Real[]: Y list of Y values for the curve
    # @param Integer: i order to be used in interpolation
    # @return new CurveT object
    def __init__(self, X, Y, i):
        if(not isAscending(X)):
            raise IndepVarNotAscending("X must be ascending")
        if(len(X) != len(Y)):
            raise SeqSizeMismatch("X and Y must be same length!")
        if(i != 1 and i != 2):
            raise InvalidInterpOrder("i must be either t1 or 2")
        
        #need to store to compare if equal
        self.X = X
        self.Y = Y
                        
        self.minx = X[0]
        self.maxx = X[len(X) - 1]
        self.o = i
        self.f = lambda v: self.__interp__(X, Y, self.o, v)

    def __interp__(self, X,Y,o,v):
        i = index(X, v)
        if(o == 1):
            return interpLin(X[i], Y[i], X[i+1], Y[i+1], v)
        else:
            return interpQuad(X[i-1], Y[i-1], X[i], Y[i], X[i+1], Y[i+1], v)
    
    ## @brief Finds the smallest x value in data
    # @return Real: smallest x-value
    def minD(self):
        return self.minx
    
    ## @brief Finds the largest x value in data
    # @return Real: largest x-value
    def maxD(self):
        return self.maxx
    
    ## @brief Returns order of interpolation of function
    # @return Integer: order of interpolation
    def order(self):
        return self.o
    
    ## @brief Approximates curve at the given point
    # @details Uses linear (o = 1) or quadratic (o = 2) interpolation to approximate value of curve at x
    # @param x Real: value to be evaluated 
    # @return Real: value of curve at x
    def eval(self, x):
        if(x > self.maxx or x < self.minx):
            raise OutOfDomain("x out of curve range")
        return self.f(x)
    
    ## @brief Approximates the first derivative of the curve
    # @details Uses forward divided difference to approximate the value at x for the first derivative of the curve
    # @param x Real: value to be evaluated 
    # @return Real: value of derivate curve at x
    def dfdx(self, x):
        if(x > self.maxx or x < self.minx):
            raise OutOfDomain("x out of curve range")
        return (self.f(x + self.DX) - self.f(x))/self.DX
    
    ## @brief Approximates the second derivative of the curve
    # @details Uses forward divided difference to approximate the value at x for the second derivative of the curve
    # @param x Real: value to be evaluated 
    # @return Real: value of second derivate curve at x
    def d2fdx2(self, x):
        if(x > self.maxx or x < self.minx):
            raise OutOfDomain("x out of curve range")
        return (self.f(x + 2*self.DX) - 2*self.f(x + self.DX) + self.f(x))/(self.DX ** 2)
    
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.o == other.o and self.X == other.X and self.Y == other.Y
        return false

            


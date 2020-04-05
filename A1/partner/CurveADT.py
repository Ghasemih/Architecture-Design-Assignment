## @file CurveADT.py
#  @author Victor Chen
#  @brief Provides the CurveT ADT class for representing sequences
#  @date 1/22/2017

import numpy

## @brief ADT representing a curve
class CurveT:

    ## @brief CurveT constructor
    #  @details Initializes a curveT object with x and y co-ordinates from an specified text file
    #  @param s the name of the text file formatted such that x and y coordinates are per line and separated by a ", "
    def __init__(self, s):
        self.x = []
        self.y = []
        
        txt = open(s, "r")
        lines = txt.readlines()
        
        for i in lines:
            splitLine = i.split(", ")
            self.x.append(int(splitLine[0]))
            self.y.append(int(splitLine[1]))

    ## @brief Returns the linear interpolation around the value of the x-coordinate
    #  @param x an integer representing the x value of the linear interpolation formula
    #  @exception Exception throw is supplied when x is not found in the coordinates or if x is out of range for the formula
    #  @return The linear interpolation around x
    def linVal(self, x: "real"):
        
        if self.x[0] == x or self.x[len(self.x) - 1] == x:
            raise Exception("X value out of range!")
        
        found = False
        for i in range(len(self.x)):
            if self.x[i] == x:
                y1 = self.y[i-1]
                y2 = self.y[i+1]
                x1 = self.x[i-1]
                x2 = self.x[i+1]
                found = True
                break

        if found:
            return ((y2 - y1) / (x2 - x1) * (x - x1)) + y1
        else:
            raise Exception("x not found!")

    ## @brief Returns the quadratic interpolation around the value of the x-coordinate
    #  @param x an integer representing the x value of the quadratic interpolation formula
    #  @exception Exception throw is supplied when x is not found in the coordinates or if x is out of range for the formula 
    #  @return The quadratic interpolation around x
    def quadVal(self, x: "real"):

        if self.x[0] == x or self.x[1] == x or self.x[len(self.x) - 1] == x:
            raise Exception("x value out of range!")
        
        found = False
        for i in range(len(self.x)):
            if self.x[i] == x:
                x0 = self.x[i-2]
                x1 = self.x[i-1]
                x2 = self.x[i+1]
                y0 = self.y[i-2]
                y1 = self.y[i-1]
                y2 = self.y[i+1]
                found = True
                break

        if found:
            return y1 + ((y2-y0)*(x-x1))/(x2-x0) + (y2 - (2*y1) + y0)*((x-x1)**2)/(2*((x2-x1)**2))
        else:
            raise Exception("X not found!")

         
    ## @brief Returns the npoly-interpolation around the value of x to the degree of n
    #  @param n the integer value representing the degree of the polynomial
    #  @param x the value on which the interpolation is being done around
    #  @return The npoly-interpolation around x
    def npolyVal(self, n: "integer degree", x: "real"):

        p = numpy.poly1d(numpy.polyfit(self.x, self.y, n))
        
        return p(x)

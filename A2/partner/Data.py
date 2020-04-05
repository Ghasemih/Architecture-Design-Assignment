## @file Data.py
# @title Data
# @author Somar Aani
# @date 07/02/2018

from CurveADT import CurveT
from SeqServices import interpLin, index, isInBounds
from Exceptions import Full, IndepVarNotAscending, InvalidIndex, OutOfDomain

## @brief Class representing data of curves
class Data:

    MAX_SIZE = 10

    ## @brief Initializes data sequences
    def init():
        Data.S = []
        Data.Z = []

    ## @brief adds values to data
    # @param s CurveT: curve to be added
    # @param z Real: independant variable to be added
    def add(s,z):
        if(len(Data.S) == Data.MAX_SIZE):
            raise Full("Data is full")
        if(len(Data.Z) != 0 and z <= Data.Z[len(Data.Z)-1]):
            raise IndepVarNotAscending("Value being added is not larger than last element")
            
        Data.S.append(s)
        Data.Z.append(z)

    ## @brief gets curve at index i
    # @param i Integer: Index of curve to be returned
    # @return CurveT: curve at index i
    def getC(i):
        if(i < 0 or i >= len(Data.S)):
            raise InvalidIndex("Index is invalid")
        return Data.S[i]

    ## @brief uses linear interpolation on data
    # @param x: approximates curves at x
    # @param z: approximates data at z
    # @return linear approximation of the data at z
    def eval(x, z):
        if(not isInBounds(Data.Z, z)):
            raise OutOfDomain("z is out of domain")
        j = index(Data.Z,z)
        return interpLin(Data.Z[j], Data.S[j].eval(x), Data.Z[j + 1], Data.S[j + 1].eval(x), z)

    ## @brief slices the data to return a new Curve 
    # @param x: approximates curves at x
    # @param i: order of interpolation for output curve
    # @return CurveT: independant variables are equivalent to data, and dependant are approximation at x
    def slice(x, i):
        Y = list(map(lambda j : (Data.S[j].eval(x)), range(len(Data.Z))))
        return CurveT(Data.Z, Y, i)
            

## @file SeqServices.py
# @title Sequence Services
# @brief library containing some sequence operations
# @author Somar Aani
# @date 07/02/2018
#

## @brief Finds out whether a list is strictly increasing 
# @param X Real[]: list to check 
# @return Bool: if the list is ascending
def isAscending(X):
    for i in range(len(X) - 1):
        if(X[i+1] < X[i]):
            return False
    return True

## @brief Finds out whether a variable is in bounds of a list
# @param X Real[]: list to check 
# @param x Real: value to check
# @return Bool: if x is in range of X
def isInBounds(X, x):
    return X[0] <= x and x <= X[len(X)-1]

## @brief Linear interpolation using 2 points
# @param x1 Real: value of x1
# @param y1 Real: value of y1
# @param x2 Real: value of x2
# @param y2 Real: value of y2
# @param x Real: value which curve is approximated at
# @return Real: approximation at x using x1,y1,x2,y2
def interpLin(x1, y1, x2, y2, x):
    return (y2 - y1)/(x2 - x1)*(x - x1) + y1

## @brief Quadratic interpolation using 3 points
# @param x1 Real: value of x0
# @param y1 Real: value of y0
# @param x1 Real: value of x1
# @param y1 Real: value of y1
# @param x2 Real: value of x2
# @param y2 Real: value of y2
# @param x Real: value which curve is approximated at
# @return Real: approximation at x using x0,y0,x1,y1,x2,y2
def interpQuad(x0,y0,x1,y1,x2,y2,x):
    return y1 + ((y2-y0)/(x2-x0))*(x - x1) + ((y2 - 2*y1 + y0)/(2 * (x2 - x1)**2))*(x - x1)**2
    
## @brief Finds the position of a value in a list
# @param X Real[]: list to check 
# @param x Real: the value of the position to be found
# @return Integer: location (i) of integer such that X(i) <= x <= X(i+1)
def index(X, x):
    for i in range(0, len(X) - 1):
        if(X[i+1] > x):
            return i

    

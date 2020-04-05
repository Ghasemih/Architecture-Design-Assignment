## @file   plot.py
#  @author Hamid Ghasemi 400028420
#  @brief  Display graphs of the sequence 
#  @date   08/02/2018

from CurveADT import *

from matplotlib import pyplot as plt

## @brief PlotSeq is a function that plots sequences 
#  @details Gets all the inputs sequence and plots the diagram based   
#  on sequence X and Y 
#  @param X is the first input sequence
#  @param Y is the second input sequence
def PlotSeq(X, Y):
    if (len(X) != len(Y)):
        raise SeqSizeMismatch ("The length of X and Y are not equal")

    
    plt.plot(X, Y, 'ro')
    plt.xlabel('x axiom')
    plt.ylabel('y axiom')
    plt.show()

## @brief PlotCurve is a function that plots a curve
#  @details Gets all the inputs sequence and plots the diagram based   
#  on sequence X and Y 
#  @param c is sequence of CurveT that user inputs
#  @param n is value that user inputs
def PlotCurve(c, n):
    if (c.order()== 2):
        X = range(c.minD() + ((c.maxD()- c.minD())/n), c.maxD() - ((c.maxD()-c.minD())/n), (c.maxD()-c.minD())/n ) 
        Y = [c.eval(x) for x in X]
        PlotSeq(X, Y)
    elif (c.order()== 1):
        X = range(c.minD(), c.maxD() - ((c.maxD()-c.minD())/n), (c.maxD()-c.minD())/n ) 
        Y = [c.eval(x) for x in X]
        PlotSeq(X, Y)

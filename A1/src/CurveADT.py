## @file   CurveADT.py
#  @author Hamid Ghasemi 400028420
#  @brief Provides the SeqT class to show the sequence
#  @date   22/1/2018


from SeqADT import *
import numpy

## @brief Making class curveT
class CurveT:
    ## @brief CurveT constructor
    #  @details It opens a textfile and reads it, then makes two arrays equal to
    #  first and second column which are bunch of numbers
    #  @param s is string that user inputs
    def __init__(self, s):
        f = open(s, 'r')
        Data = f.readlines()
        self.x = SeqT()
        self.y = SeqT()
        Num = [ ]
        for i in Data:
            Num = i.split(', ')
            self.x.seq.append(float(Num[0]))
            self.y.seq.append(float(Num[1]))
        f.close()


    ## @brief linVal is a function that using interpolation between data values
    #  @details Use the input value that user inserts and find the interpolation
    #  between numbers before and after the input value that present in the sequence
    #  @param x is the input value
    #  @return y is the value that returns at the end
    def linVal(self, x):
        d = self.x.indexInSeq(x)
               
        x1 = self.x.seq[d]
        x2 = self.x.seq[d+1]
        
        y1 = self.y.seq[d]
        y2 = self.y.seq[d+1]

        if (x2 - x1 == 0):
            print ("Error, there is zero in denominator")
        else:
            y = ((y2-y1)/(x2-x1))*(x-x1) + y1
            return y
    
    ## @brief quadVal is a function that using interpolation between data values
    #  @details Use the input value that user inserts and find the interpolation
    #  between numbers before and after the input value that present in the sequence
    #  @param x is the input value
    #  @return y is the value that returns at the end
    def quadVal(self, x):
        d = self.x.indexInSeq(x)
        if d == 0:
            print ("There is no number for x0 and y0")
        else:   
            x0 = self.x.seq[d-1]
            x1 = self.x.seq[d]
            x2 = self.x.seq[d+1]

            y0 = self.y.seq[d-1]
            y1 = self.y.seq[d]
            y2 = self.y.seq[d+1]

            if (x2 - x0 == 0) or (x2 - x1 == 0):
                print ("Error, there is zero in denominator")
            else :
                y = y1 + ((y2-y0)/(x2-x0))*(x-x1)+((y2-2*y1+y0)/(2*((x2-x1)**2))*(x-x1)**2)
                return y
            
    ## @brief npolyVal is a function that finds approximatation value 
    #  @details It makes the line of best fit for polynomials
    #  @param n is the integer value that user inputs
    #  @param x is the real value which user inputs
    #  @return y is the value that is best fit that returns at the end 
    def npolyVal(self, n, x):
        x_seq = self.x.seq
        y_seq = self.y.seq
        line = numpy.polyfit(x_seq, y_seq, n)
        y = numpy.polyval(line, x)
        return y
        

        
        
        

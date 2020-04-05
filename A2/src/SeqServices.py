## @file   SeqServices.py
#  @author Hamid Ghasemi 400028420
#  @brief  Provides some functions
#  @date   08/02/2018


## @brief isAscending is a function that check if the array is ascending
#  @details Uses the input sequence that user inserts and check if the sequence
#  is ascending or not
#  @param X is the input sequence
#  @return Boolean value True or False
def isAscending(X):
    for i in range (0, len(X)-2):
        if X[i+1] < X[i]:
            return False
        
    return True


## @brief isInBounds is a function 
#  @details Uses the input value and sequence that user inserts and check if the value
#  is within sequence.
#  @param X is the input sequence
#  @param x is input value 
#  @return Boolean value True if value of x is within sequence or False        
def isInBounds(X,x):
    if (X[0] <= x and x <= X[len(X)-1]):
        return True
    else:
        return False
    

## @brief interpLin is a function 
#  @details Uses the input values that user inserts and find the interpolation linear
#  between all the values
#  @param x1 is input value
#  @param y1 is input value
#  @param x2 is input value
#  @param y2 is input value
#  @param x is input value
#  @return y that is made by x1,y1,x2,y2,x values
def interpLin(x1,y1,x2,y2,x):
    if (x2 - x1 == 0):
        print ("Error, denominator is zero")
    else:
        y = ((y2-y1)/(x2-x1))*(x-x1) + y1
        return y
## @brief interpLin is a function 
#  @details Uses the input values that user inserts and find the interpolation quadratic
#  by using all the values
#  @param x0 is input value
#  @param y0 is input value
#  @param x1 is input value
#  @param y1 is input value
#  @param x2 is input value
#  @param y2 is input value
#  @param x  is input value
#  @return y that is made by x1,y1,x2,y2,x values

def interpQuad(x0,y0,x1,y1,x2,y2,x):
    
    if (x2 - x0 == 0) or (x2 - x1 == 0):
        print ("Error, there is zero in denominator")
    else :
        y = y1 + ((y2-y0)/(x2-x0))*(x-x1)+((y2-2*y1+y0)/(2*((x2-x1)**2))*(x-x1)**2)
        return y

def index(X,x):
    for i in range (0, len(X)-1):
        if (X[i] <= x and  x < X[i+1]):
            return i
        

    

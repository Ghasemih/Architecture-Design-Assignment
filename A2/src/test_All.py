from CurveADT import *
from Data import *
from SeqServices import *


def test_isAscending():
    assert isAscending([1, 3 ,4 ,5]) == True
    assert isAscending([3, 3 ,4 ,5]) == False
    assert isAscending([3, 4 ,2 ,5]) == False

def test_isInBounds():
    assert isInBounds([1, 3 ,4 ,5],6) == False
    assert isInBounds([1, 3 ,4 ,5],2) == True
    assert isInBounds([1, 3 ,4 ,5],5) == True

def test_interpLin():
    assert interpLin(5,1,6,1,3) == 0
    assert interpLin(1,2,5,12,2) == 4.5
    assert interpLin(1,1,2,2,3) == 4

def test_interpQuad():
    assert interpLin(3,0,1,4,2,0,1) == 4
    assert interpLin(2,1,3,4,1,3,1) == 6


def test_index():
    assert index([1, 3 ,4 ,5],3) == 1
    assert index([1, 3 ,4 ,5],4) == 2
    assert index([1, 3 ,4 ,5, 6, 10, 16],12) == 5

############################

x = Data()
x.init()
x.S = [ 1, 3 , 4 , 5]
def test_init():
    assert x.S[0] == 1
    assert x.Z == []
    assert x.S[3] == 5

def test_add():
    x.add(1, 2) 
    assert x.S == [ 1, 3 , 4 , 5, 1]
    assert x.Z == [2]
    assert x.S[3] == 5

def test_getC():
    assert x.getC(2)== 4
    assert x.getC(0)== 1

#def test_eval():
    
#def test_slice():
    
############################
X= [1, 2 ,3 ,10]
Y=[2, 4, 5, 7]
i= 2
x = CurveT(X, Y, i)

#def test_interp():


def test_minD():
    assert x.minD() == 1

def test_maxD():
    assert x.maxD() == 10

def test_order():
    assert x.order() == 2
    
def test_aval():
    assert x.eval(11) == 'OutOFDomain'

def test_dfdx():
    assert x.dfdx(21) == 'OutOFDomain'

def test_d2fdx2():
    assert x.d2fdx2(21) == 'OutOFDomain'

  


    





    

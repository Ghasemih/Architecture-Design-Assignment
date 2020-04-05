## @file   testSeqs.py
#  @author Hamid Ghasemi 400028420
#  @brief Provides the SeqT class to show the sequence
#  @date   22/1/2018


from SeqADT import *
from CurveADT import *

##  @brief Tests the add funtion method of the SeqT class
#   @detail Checks for the index in sequence, if i is within the length it will add otherwise it adds at the end
#   the value to its desired position else at the end of the list
t = SeqT()
def test_add():
    t.add(0, 1)
    t.add(1, 2)
    t.add(2, 3)
    t.add(1, 4)
    # t = [1, 4, 2, 3]
    try:
        assert t.seq[0] == 1 and t.seq[1] == 4
        print ("add test passed")
    except AssertionError:
        print ("add test failed")
        
## @brief test_rm function remove the value that user has input 
#  @detail If index i is in the list return a value
#   return value
def test_rm():
    # t = [1, 4, 2, 3]
    t.rm(1)
    # t = [1, 2, 3]
    try:
        assert t.seq[1] == 2
        print ("remove test passed")
    except AssertionError:
        print ("remove test failed")
        
## @brief test_set it tests and set value 
#  @detail Test the cases where input i is in the list
#   set a value 3 to 4
def test_set():
    # t = [1, 2, 3]
    t.set(2, 4)
    # t = [1, 2, 4]
    try:
        assert t.seq[2] == 4
        print ("set test passed")
    except AssertionError:
        print ("set test failed")
        
## @brief test_get tests if the required value is outputted 
#  @detail Test the cases where input i (index) is in the list
#   return value 2 
def test_get():
    # t = [1, 2, 4]
    t.get(1)
    # t [1] = 2
    try:
        assert t.seq[1] == 2
        print ("get test passed")
    except AssertionError:
        print ("get test failed")

## @brief Verifies the size of the sequence
def test_size():
    # t = [1, 2, 4]
    try:
        assert t.size() == 3
        print ("size test passed")
    except AssertionError:
        print ("size test failed")

## @brief tests if the input value is between two numbers within a sequence
# @detail a real value in the middle
# it must return a index 1
def test_indexInSeq():
    # t = [1, 2, 4]
    # after using indexInSeq it should give us i = 0
    t.indexInSeq(3)
    try:
        assert t.indexInSeq(3) == 1
        print ("indexinseq test passed")
    except AssertionError:
        print ("indexinseq test failed")

"TESTING CurveADT File"

## @brief Tests the y from the method linVal
#  @detail checks for value within a value in the middle of the sequence
#  Check a value within the sequence          
d = CurveT("1.txt")
def test_linVal(x):
    # xcontains: x = [1, 3, 4, 6] 
    # ycontains: y = [4, 6, 8, 11]
    
    d.linVal(3.4)
    try:
        assert d.linVal(3.4) == 6.8
        print ("linVal test passed")
    except AssertionError:
        print ("linVal test failed")

## @brief Tests the yvalue from the method quadVal
#  @detail checks for value within a value in the middle of the sequence
#   Check value whithin sequence  
def test_quadVal(x):
    # xcontains: x = [1, 3, 4, 6] 
    # ycontains: y = [4, 6, 8, 11]
    
    d.quadVal(3.4)
    try:
        assert round(d.quadVal(3.4)) == 7
        print ("quadVal test passed")
    except AssertionError:
        print ("quadVal test failed")
        
## @brief npolyVal tests the y value with n degree
#  @detail input number is 1 for n and 3 for x which return 6.54
def test_npolyval(n, x):
    # xcontains: x = [1, 3, 4, 6] 
    # ycontains: y = [4, 6, 8, 11]
    c = d.npolyVal(1,3)
    try:
        
        assert round(c, 2) == 6.54
        print ("npolyval test passed")
    except AssertionError:
        print ("npolyval test failed")



test_add()
test_rm()
test_set()
test_get()
test_size()
test_indexInSeq()
test_linVal("1.txt")
test_quadVal("1.txt")
test_npolyval(1, 3)
        






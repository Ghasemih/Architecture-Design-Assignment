## @file SeqADT.py
#  @author Victor Chen
#  @brief Provides the SeqT ADT class for representing sequences
#  @date 1/22/2017

## @brief ADT representing a sequence
class SeqT:

    ## @brief SeqT constructor
    #  @details Initializes a SeqT object with an empty sequence.
    def __init__(self):
        self.sequence = []

    ## @brief Adds a new value to the sequence
    #  @param i an integer representing the index to add a new value
    #  @param v a real number to add to the sequence at index i
    #  @exception Exception throws is supplied index is greater than length of the sequence or a negative value
    def add(self, i: "int index", v: "real to add"):
        #values can only be added within the existing sequence, or
        #immediately after the last entry
        if self.sequence == [] and i != 0:
            raise Exception("Sequence currently empty! Use index at 0!")
        elif i > len(self.sequence):
            raise Exception("Index greater than sequence length!")
        elif i < 0:
            raise Exception("Index cannot be smaller than zero!")
        
        if i == len(self.sequence):
            self.sequence.append(v)
        else:
            temp = self.sequence[0:i]
            temp.append(v)
            for index in range(len(self.sequence)-i):
                temp.append(self.sequence[index+i])
                self.sequence = temp

    ## @brief Returns the element at index i in the sequence and pops it from the sequence, reducing the sequence length by 1
    #  @param i an integer representing the index of the element to be removed
    #  @exception Exception throws is supplied index is greater than length of the sequence or a negative value
    #  @return The removed element
    def rm(self, i: "int index to be removed"):
        try:
            self.sequence.pop(i)
        except:
            if i < 0:
                raise Exception("Index cannot be smaller than zero!")
            elif i > len(self.sequence):
                raise Exception("Index greater than sequence length!")

    ## @brief Replaces the value at i with the value of v
    #  @param i an integer representing the index of the element to be replaced
    #  @param v the value to replace the element at index i
    #  @exception Exception throws is supplied index is greater than length of the sequence or a negative value
    def set(self, i: "int index", v: "real"):
        try:
            self.sequence[i] = v
        except:
            if i < 0:
                raise Exception("Index cannot be smaller than zero!")
            elif i > len(self.sequence):
                raise Exception("Index greater than sequence length!")

    ## @brief Returns the current size of the sequence
    #  @return The integer length of the sequence
    def size(self):
        return len(self.sequence)

    ## @brief Returns an index i such that SeqT.get(i) <= v <= SeqT.get(i+1)
    #  @param v the real value being searched for
    #  @return The integer value of the index at which v appears
    #  @exception returns -1 when element v does not exist in the sequence
    def indexInSeq(self, v: "real"):
        for i in range(len(self.sequence)):
            if self.sequence[i] == v:
                return i
        return -1

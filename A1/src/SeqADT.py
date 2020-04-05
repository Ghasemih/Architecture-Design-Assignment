## @file   SeqADT.py
#  @author Hamid Ghasemi 400028420
#  @brief Provides the SeqT class to show the sequence
#  @date   22/1/2018


## @brief Making a sequences 
class SeqT:
    ## @brief SeqADT constructor
    #  @details it makes an empty sequence
    def __init__(self):
        self.seq = []

    ## @brief Adds number to sequence
    #  @details It adds value to the sequence based on the index number 
    #  @param i is the index of the sequence
    #  @param v is the value that user inputs

    def add(self, i, v):
        if len(self.seq) < i:
            self.seq.append(v)
        else:
            self.seq.insert(i, v)
    
    ## @brief rm removes the values from the sequence based on the index number
    #  @param i is the index of the sequence        
    def rm(self, i):
        del self.seq[i]
        
    ## @brief set set number of the sequence with number that user inputs
    #  @param i is the index of the sequence
    #  @param v is the value 
    def set(self, i,v):
        self.seq[i] = v

    ## @brief get get numbers by using index from sequence
    #  @param i is the index of the sequence
    #  @return The number that user looks for based on the index     
    def get(self, i):
        if i > len(self.seq)-1:
            print ("Value is out of boundary")
        else:
            return self.seq[i]
        
    ## @brief Size Shows the length of the sequence 
    #  @return The length of the sequence 
    def size(self):
          return len(self.seq)      

    ## @brief indexInSeq Checks if value is in the range, and it finds 
    #   number before the value which user inputs in sequence and finds its index
    #  @param v is value that function gets from the user
    #  @return i The index of the sequence
    def indexInSeq(self, v):
        for i in range (0, len(self.seq)-1):
            if (self.get(i) <= v and  v <= self.get(i+1)):
                return i
            

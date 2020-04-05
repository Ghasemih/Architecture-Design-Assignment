## @file   Load.py
#  @author Hamid Ghasemi 400028420
#  @brief  Read data from the file infile associated with the string s
#  @date   08/02/2018

import csv
from CurveADT import *
from Data import *

## @brief Initializes four empty sequences
#  @details reads a textfile with data of a polynomial and save x and y in return
def Load(s):
    k = Data()
    k.init()
    o = []
    x = []
    y = []
    with open(s) as csvfile:
            lines = csv.reader(csvfile, delimiter = ',')
            number = 0
            for row in lines:
                if number == 0:
                    for i in range(0, len(row), 1):
                        k.Z.append(float(row[i]))
                    m = len(k.Z)
                    x = [[0 for x in range(1)] for y in range(m)]
                    y = [[0 for x in range(1)] for y in range(m)]
                    number += 1
                elif number == 1:
                    for i in range(0, len(row), 1):
                        o.append(float(row[i]))
                    number += 1
                else:
                    data = 0
                    for i in range(0, 2*m - 1, 2):
                        a = row[i]
                        b = row[i + 1]
                        if a != '' or b != '':
                            x[data].append(float(a))
                            y[data].append(float(b))
                        data += 1

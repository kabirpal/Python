#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    
    for i in range(len(arr)):
        if arr[i] > 0:
            pos += 1
            i += 1
        elif arr[i] == 0:
            zero += 1
            i+= 1
        else:
            neg += 1
            i += 1
    print(round(pos/n,6))
    print(round(neg/n,6))
    print(round(zero/n,6))          

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)


"""
Sample Input

STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

Sample Output

0.500000
0.333333
0.166667
"""
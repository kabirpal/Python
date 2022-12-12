'''
Sample Input

1 2 3 4 5
Sample Output

10 14
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    j = len(arr)
    add = 0
    for i in range(j-1):
        add = add + arr[i]
        i += 1
    arr.reverse()
    revadd = 0
    for i in range(j-1):
        revadd = revadd + arr[i]
        i+= 1
    print(add)
    print(revadd)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

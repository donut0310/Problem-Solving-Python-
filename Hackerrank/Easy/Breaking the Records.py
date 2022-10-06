#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    min_cnt, max_cnt = 0, 0
    minm, maxm = scores[0], scores[0]
    
    for i in range(1, len(scores)):
        if scores[i] < minm:
            min_cnt += 1
            minm = scores[i]
        elif scores[i] > maxm:
            max_cnt += 1
            maxm = scores[i]
    return max_cnt, min_cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from itertools import combinations
#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#
def find(node, table):
    if table[node] == node: return node
    else: return find(table[node], table)

def union(a, b, table):
    parent_a = find(a, table)
    parent_b = find(b, table)
    if a < b: table[parent_b] = table[parent_a]
    else: table[parent_a] = table[parent_b]

def journeyToMoon(n, astronaut):
    answer = 0
    table = {}
    
    for i in range(n): # initiate parent table
        table[i] = i
    
    for a,b in astronaut:
        union(a,b,table) # call union-find alg

    _dict = defaultdict(int)
    for node in table:
        parent = find(node, table) # find parent node of current node, because there's no update current nodes's parent in method find()
        _dict[parent] += 1

    answer = sum([_dict[a] * (n - _dict[a]) for a in _dict]) // 2 # {a(n-a) + b(n-b) + c(n-c)} // 2 
    return answer

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()

# 5 3
# 0 1
# 2 3
# 0 4
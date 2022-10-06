#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    index = 0
    set_rank = sorted(list(set(ranked)), reverse=True)
    result = []
    
    for i in range(len(player)):

        if i != 0: del set_rank[index]

        left, right = 0, len(set_rank) - 1
        score = player[i]
        
        while left <= right:
            mid = (left + right) // 2

            if set_rank[mid] > score: 
                left = mid + 1
            elif set_rank[mid] < score:
                right = mid - 1
            else: 
                left = mid
                del set_rank[left]
                break
            
        set_rank.insert(left, score)
        index = left
        result.append(index + 1)
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

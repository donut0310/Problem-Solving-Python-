#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
import heapq
#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    graph = defaultdict(set) # list로 하면 TEST-INPUT에 중복값이 적용되어있어 런타임 에러 발생
    dist = [math.inf] * (n+1)
        
    for u,v in edges:
        graph[u].add((v, 6))
        graph[v].add((u, 6))

    queue = [(s,0)]
    while queue:
        node, d = heapq.heappop(queue)

        if d > dist[node]: continue
        dist[node] = d

        for next_node, w in graph[node]:
            weight = d + w
            if weight < dist[next_node]:
                heapq.heappush(queue, (next_node, weight))

    answer = []
    for i in range(1, n+1):
        if i == s: continue
        d = dist[i]
        
        if d < math.inf: answer.append(d)
        else: answer.append(-1)  
        
    return answer
        
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

    #     fptr.write(' '.join(map(str, result)))
    #     fptr.write('\n')

    # fptr.close()

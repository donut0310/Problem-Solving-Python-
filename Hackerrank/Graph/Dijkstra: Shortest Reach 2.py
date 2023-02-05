#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
import heapq
#
# Complete the 'shortestReach' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER s
#

def shortestReach(n, edges, s):
    graph = defaultdict(list)
    dist = {}
    visited = defaultdict(int)
    
    for i in range(1, n+1):
        dist[i] = math.inf
    
    for u,v,w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    queue = [(s,0)]
    
    while queue:
        node, d = heapq.heappop(queue)
        if d > dist[node]: continue
        dist[node] = d
        
        for next_node, w in graph[node]:
            weight = w + d
            if weight > dist[next_node]: continue

            heapq.heappush(queue, (next_node, weight))
    
    answer = []
    for i in range(1, n+1):
        d = dist[i]
        if d==0: continue
        if d < math.inf: answer.append(d)
        else: answer.append(-1)
    
    return answer
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = set()
        for _ in range(m):
            x, y, z = map(int, input().rstrip().split())
            edges.add((x, y, z))
        # edges = set()

        # for _ in range(m):
        #     edges.add(list(map(int, sys.stdin.readline().rstrip().split())))
            

        s = int(input().strip())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

'''
문제에서 제공하는 간선 간의 정보를 저장하는 구문에 있어서 문제의 오류를 발견

shortestReach 메소드 내에서 중복 간선 처리를 했으나 계속해서 Runtime Error가 발생

메인 함수에서 간선 간의 정보를 저장하는 구문(주석 처리된)에서 중복 간선 처리를 진행하니 TC 7를 해결할 수 있었다.

간단한 다익스트라 알고리즘 적용 문제였으나 입출력 부분에서의 문제 오류로 장시간 삽질을..
'''
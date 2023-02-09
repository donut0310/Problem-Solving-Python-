#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

def dfs(current_node, cnt, graph, graph_cnt):
    for next_node in graph[current_node]:
        graph_cnt[current_node] += dfs(next_node, 0, graph, graph_cnt)

    graph_cnt[current_node] += 1
    return graph_cnt[current_node]

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    visited = [0] * (t_nodes + 1)
    graph = defaultdict(list)
    graph_cnt = defaultdict(int)
    answer = 0
    
    # make graph
    for i in range(t_edges):
        if t_from[i] < t_to[i]: graph[t_from[i]].append(t_to[i])
        else: graph[t_to[i]].append(t_from[i])
        
        
    # dfs -> get sum of all child nodes of current node with count 1(current_node)
    dfs(1, 0, graph, graph_cnt)
        
    # bfs -> check even Tree
    queue = graph[1] # start node
    while queue:
        node = queue.pop()
        if graph_cnt[node] % 2 == 0: answer += 1
        
        for next_node in graph[node]:
            queue.append(next_node)
    
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()

'''
조건 1: 전체 노드의 수는 짝수가 보장

<풀이>
1. 각 노드마다 자신을 포함한 값과 자식노드의 개수를 dfs를 사용해 카운팅하고 dictionary(graph_cnt)에 저장한다.
2. 루트노드의 자식노드들을 큐에 담고 bfs를 사용해 각 노드마다 graph_cnt에서 짝수인 노드를 카운팅한다.
2-1. graph_cnt값이 짝수인 노드는 even Tree로 분리될 수 있기 때문에 가장 작은 짝수 단위로 구분이 가능하다.
'''
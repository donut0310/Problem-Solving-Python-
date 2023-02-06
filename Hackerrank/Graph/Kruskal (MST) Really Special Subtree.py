#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

# find root node of each node
def find(node, table):
    if node == table[node]: return node
    else: return find(table[node], table)

# union root node of both nodes
def union(node1, node2, table):
    parent1 = find(node1, table)
    parent2 = find(node2, table)
    if parent1 == parent2: return False
    if parent1 < parent2: table[parent2] = parent1
    else: table[parent1] = parent2
    return True

def kruskals(g_nodes, g_from, g_to, g_weight):
    table = [0] * (g_nodes + 1)
    
    for i in range(1, g_nodes + 1):
        table[i] = i
    
    # make edges information
    edges_info = []
    for i in range(len(g_from)):
        edges_info.append((g_from[i], g_to[i], g_weight[i]))
        
    edges_info.sort(key=lambda x:x[2])

    # Kruskals Alg
    answer, cnt = 0, 0
    for node1, node2, weight in edges_info:
        if union(node1, node2, table):
            answer += weight
            cnt += 1
        if cnt == g_nodes-1: # check all edges
            break
    
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    fptr.write(str(res) + '\n')
    fptr.close()

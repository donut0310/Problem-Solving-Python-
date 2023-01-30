import math
import os
import random
import re
import sys
from collections import defaultdict,deque

def roadsAndLibraries(n, c_lib, c_road, cities):
    visited = [0] * (n+1)
    graph = defaultdict(list)
    min_cost = 0

    for u,v in cities:
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n+1):
        if visited[i]: continue
        queue = deque([i])
        city_cnt = 0

        while queue:
            node = queue.popleft()
            if visited[node]: continue

            visited[node] = 1
            city_cnt += 1

            for next_node in graph[node]:
                if not visited[next_node]:
                    queue.append(next_node)

        min_cost += min((city_cnt-1) * c_road + c_lib, city_cnt * c_lib)

    return min_cost

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print('\n',result)
        # fptr.write(str(result) + '\n')

    # fptr.close()

# 2           
# 3 3 2 1     
# 1 2         
# 3 1
# 2 3
# 6 6 2 5
# 1 3
# 3 4
# 2 4
# 1 2
# 2 3
# 5 6
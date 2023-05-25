from collections import defaultdict
import sys
input = sys.stdin.readline

def solution():
    answer = -1
    visited = [0] * (n+1)
    stack = [1]
    
    while stack:
        node = stack.pop()
        if visited[node]: continue

        visited[node] = 1
        answer += 1

        for next_node in graph[node]:
            if not visited[next_node]: stack.append(next_node)

    return answer

n = int(input())
pair = int(input())
graph = defaultdict(list)

for i in range(pair):
    u, v = map(int, input().rstrip().split(' '))    
    graph[u].append(v)
    graph[v].append(u)
    
print(solution())




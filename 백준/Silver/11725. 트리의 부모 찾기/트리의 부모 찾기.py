from collections import defaultdict
import sys
input = sys.stdin.readline

def solution():
    answer = 0
    stack = [1]
    p_dict = {}

    for i in range(n):
        p_dict[i+1] = 0

    visited = [0] * (n+1)

    while stack:
        node = stack.pop()
        if visited[node]: continue
        visited[node] = 1

        for child in tree[node]:
            if not visited[child]:
                p_dict[child] = node
                stack.append(child)

    for i in range(2, n+1):
        print(p_dict[i])

n = int(input())
tree = defaultdict(list)

for i in range(n-1):
    u, v = map(int, input().rstrip().split(' '))    
    tree[u].append(v)
    tree[v].append(u)

solution()
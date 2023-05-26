from collections import defaultdict
import sys
input = sys.stdin.readline

def dfs(v, d):
    global answer

    if v == v2: # 타겟 노드를 만나면 반환
        answer = d
        return
    
    visited[v] = 1
    
    # 자식 노드로 재귀
    for child in childs_info[v]:
        if not visited[child]: dfs(child, d + 1)

    # 부모 노드로 재귀
    p = parent_info[v]
    if p and not visited[p]: dfs(p, d + 1)

    return

def solution():   
    global answer 
    visited[v1] = 1
    dfs(v1, 0)
    return answer if answer else -1

n = int(input())
v1, v2 = map(int, input().rstrip().split(' '))
t = int(input())
parent_info, childs_info = defaultdict(int), defaultdict(list)
visited = [0] * (n+1)
answer = 0

for i in range(t):
    p, c = map(int, input().rstrip().split(' '))
    parent_info[c] = p
    childs_info[p].append(c)

print(solution())

'''
a, b의 촌수 관계
a가 b의 상위에 존재하는 경우
b가 a의 상위에 존재하는 경우
a와 b가 서로 공통된 상위 노드를 가지는 경우
    공통된 상위 노드가 루트인 경우
    루트가 아닌 경우
a와 b가 서로 전혀 관계 없는 경우

1. 현재 노드의 부모 노드가 가진 형제 노드 중에 타겟 노드가 있는지 확인
2. 타겟 노드가 없다면 부모 노드의 부모 노드로 올라감
3. 1-2 과정 반복
4. 타겟 노드를 만나면 그때의 거리(촌수)를 반환
5. 모든 노드를 확인했음에도 타겟 노드를 찾지 못한 경우 -> -1 반환
'''
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(tree, node, answer, visited):
    visited[node] = 1
     # 현재 노드의 자식 노드 수
    childs = len(tree[node])
    
    # 리프 노드인 경우, 바로 리턴
    for next_node in tree[node]:
        if visited[next_node]: childs -= 1
    if not childs:
        return answer, False
    
    # 비단말 노드인 경우 자식 노드 재귀 탐색
    flag = False

    for next_node in tree[node]:
        if not visited[next_node]:
            answer, flag = dfs(tree, next_node, answer, visited)
            if flag: 
                childs -= 1
    # 자식 노드의 모든 스위치가 켜져있지 않은 경우(not flag), 현재 노드의 스위치를 켠다.
    # 자식 노드의 스위치 중 하나라도 켜져있지 않은 경우, 역시 현재 노드의 스위치를 켠다 => tc 1 
    # => 자식 노드가 모두 켜져있다면 현재 노드는 키지 않는다.
    if not childs:
        return answer, False
    else:
        return answer+1, True
    

def solution(n, lighthouse):
    answer = 0
    tree = defaultdict(list)
    visited = [0] * (n+1)
    
    for l1, l2 in lighthouse:
        tree[l1].append(l2)
        tree[l2].append(l1)
        
    answer, flag = dfs(tree, 1, answer, visited)
    return answer

'''
1. 등대 번호가 작은 등대에 번호가 큰 등대를 자식노드로 연결해 트리 구조를 만든다.
2. 임의의 등대를 기준으로 잡고 아래 조건을 탐색한다.

조건 1. 자식 노드(등대)가 모두 꺼져있다면 현재 노드(등대)를 킨다.
조건 2. 자식 노드(등대)가 하나라도 꺼져있다면 현재 노드(등대)를 킨다.
'''
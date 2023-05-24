import sys
input = sys.stdin.readline

def find(node):
    if node == table[node]: return node
    return find(table[node])

def union(u, v):
    p1, p2 = find(u), find(v)
    if p1 == p2: return False
    elif p1 < p2: table[p2] = p1
    else: table[p1] = p2

    return True

def solution():
    answer, edge_cnt = 0, 0

    for u, v, c in edges:
        if union(u-1, v-1):
            edge_cnt += 1
            answer += c
        if edge_cnt == n-1: break    

    return answer

n = int(input()) # 컴퓨터 수
m = int(input()) # 간선 수
edges = [] # 간선 정보
table = [i for i in range(n)] # 부모-자식 노드 연관관계 테이블

for i in range(m):
    u, v, c = map(int, input().rstrip().split(' '))
    edges.append((u, v, c))

edges.sort(key=lambda x:x[2])

print(solution())


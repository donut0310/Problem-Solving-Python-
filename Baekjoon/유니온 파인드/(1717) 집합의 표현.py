import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
table = [0] * (n+1)
for i in range(n + 1): # 초기 집합 
    table[i] = i

def find(num):
    if table[num] == num: return num
    p = find(table[num])
    table[num] = p
    return p

def union(num1, num2):
    p1 = find(num1)
    p2 = find(num2)
    if p1 == p2: return 
    elif p1 < p2: table[p2] = p1
    else: table[p1] = p2
    return 

def solution():
    for _ in range(m):
        exe, num1, num2 = map(int, input().split())
        if exe: 
            if find(num1) != find(num2): print('NO')
            else: print('YES')
        else: # 합집합
            union(num1, num2)
solution()

'''
합집합 => 두 원소의 집합이 동일한지 확인
    두 원소의 루트가 다르다면 두 번째 원소의 루트를 첫 번째 원소의 루트로 변경
    두 원소의 루트가 같다면 스킵

집합 확인 => 유니온 파인드
   
'''
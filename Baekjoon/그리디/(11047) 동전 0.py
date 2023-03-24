import sys
input = sys.stdin.readline

coins = []
n, k = map(int, input().split(' '))

for i in range(n):
    coins.append(int(input()))

def solution():
    answer = 0
    global k
    tmp = n - 1

    while k:
        if coins[tmp] > k:
            tmp -= 1
            continue
        answer += k // coins[tmp]
        k %= coins[tmp]

    print(answer) 

solution()
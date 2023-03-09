import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split(' '))
    arr = [[0] * (n+1)]
    for i in range(n):
        tmp = [0]
        tmp += list(map(int, input().split(' ')))
        arr.append(tmp)
    
    # 전체 구간 합 구하기
    for i in range(1, n+1):
        for j in range(1, n+1):
            arr[i][j] += arr[i][j-1]
            
    for i in range(1, n+1):
        for j in range(1, n+1):
            arr[i][j] += arr[i-1][j]

    # 입력 범위의 합 구하기
    for i in range(m):
        x1, y1, x2, y2 = map(int, input().split(' '))
        s = arr[x2][y2] - arr[x2][y1-1] - arr[x1-1][y2] + arr[x1-1][y1-1]
        print(s)
    return

solution()
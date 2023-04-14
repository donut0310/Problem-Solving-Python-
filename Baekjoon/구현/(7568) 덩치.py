import sys
input = sys.stdin.readline

n = int(input())
arr = [[i+1]+list(map(int, input().split(' '))) for i in range(n)]

def solution():
    answer = ''
    rank = []
    arr.sort(key=lambda x:(-x[1], -x[2]))
    
    for i in range(n):
        cnt = 0
        if i!=0: 
            for j in range(i):
                if arr[i][1] < arr[j][1] and arr[i][2] < arr[j][2]: cnt += 1
        rank.append((arr[i][0], cnt+1))

    rank.sort(key=lambda x:x[0])
    tmp = [str(i[1]) for i in rank]
    answer = ' '.join(tmp)
    return answer

print(solution())
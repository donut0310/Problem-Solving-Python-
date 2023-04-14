import sys
input = sys.stdin.readline

n, k = map(int, input().split(' '))
arr = [list(map(int, input().split( ))) for i in range(n)]

def solution():
    arr.sort(key=lambda x:(-x[1], -x[2], -x[3]))
    
    answer, same = 0, 0
    for i in range(n):
        if i==0: answer = 1
        else:
            if arr[i][1] == arr[i-1][1] and arr[i][2] == arr[i-1][2] and arr[i][3] == arr[i-1][3]: same += 1
            else: 
                answer += 1 + same
                same = 0
        if arr[i][0]==k: return answer
        
print(solution())
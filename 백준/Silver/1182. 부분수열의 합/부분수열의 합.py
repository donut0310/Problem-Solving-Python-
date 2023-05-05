import sys
input = sys.stdin.readline

n, s = map(int, input().split(' '))
arr = list(map(int, input().rstrip().split(' ')))    
answer = 0

def dfs(idx, _sum):
    global answer

    if idx >= n: return

    _sum += arr[idx]
    if _sum == s: answer += 1

    dfs(idx+1, _sum - arr[idx])
    dfs(idx+1, _sum)    

dfs(0, 0)
print(answer)


'''
부분 수열의 합이기 때문에 원소를 포함한 경우와 포함하지 않은 경우, 2가지를 고려해야한다.
따라서 재귀함수로 dfs를 각각의 경우에 한 번씩 호출해준다.
'''
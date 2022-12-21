import sys
n,k = map(int, sys.stdin.readline().split(' '))

arr = [i for i in range(1, n+1)]
answer = []
start = 0

while arr:
    index = (start + k % len(arr) - 1) % len(arr)
    answer.append(arr[index])
    arr.pop(index)
    start = index
    
print('<', end='')
for i in range(n):
    if i == n-1: print(f'{answer[i]}>', end='')
    else: print(f'{answer[i]}, ', end='')
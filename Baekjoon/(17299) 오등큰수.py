from collections import defaultdict
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))
dict = defaultdict(int)

for i in arr:
    dict[i] += 1

stack = []
answer = []

for i in range(n-1, -1, -1):
    while stack and dict[arr[i]] >= dict[stack[-1]]:
        stack.pop()
    
    if not stack:
        answer.append(-1)        
    else:
        answer.append(stack[-1])
    stack.append(arr[i])

for i in range(n-1, -1, -1):
    print(answer[i], end=' ')
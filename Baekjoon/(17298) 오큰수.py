import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split(' ')))

stack = []
answer = []

for i in range(len(arr)-1,-1,-1):
    while stack and arr[i] >= stack[-1]:
        stack.pop()
    
    if not stack: answer.append(-1)
    else: answer.append(stack[-1])
    stack.append(arr[i])
    
for i in range(n-1, -1, -1):
    print(answer[i], end=' ')
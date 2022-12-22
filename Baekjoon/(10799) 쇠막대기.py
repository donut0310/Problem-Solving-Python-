import sys

arr = sys.stdin.readline().strip()
stack = []
answer = 0
prev = ''

for i in arr:
    if i == '(':
        stack.append(i)
        prev = '('
    else:
        stack.pop()
        if prev == '(': answer += len(stack)
        else: answer += 1
        prev = ')'
print(answer)
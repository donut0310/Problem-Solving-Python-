import sys

def check(ps):
    stack = []

    for i in ps:
        if stack:
            if stack[-1] != i: stack.pop()
            else: stack.append(i)    
        else:
            if i == ')': return False
            else: stack.append(i)

    if stack: return False
    else: return True

lines = int(sys.stdin.readline())

for _ in range(lines):
    if check(sys.stdin.readline().strip()): print('YES')
    else: print('NO')

        
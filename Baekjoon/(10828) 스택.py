import sys

lines = int(sys.stdin.readline())
stack = []

for _ in range(lines):
    exe = sys.stdin.readline().strip().split(' ')

    if exe[0] == 'push':
        stack.append(int(exe[1]))
    elif exe[0] == 'pop':
        if len(stack): print(stack.pop())
        else: print(-1)
    elif exe[0] == 'size':
        print(len(stack))
    elif exe[0] == 'empty':
        if len(stack): print(0)
        else: print(1)
    elif exe[0] == 'top':
        if len(stack): print(stack[-1])
        else: print(-1)

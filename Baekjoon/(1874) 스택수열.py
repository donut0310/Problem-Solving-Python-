import sys

size = int(sys.stdin.readline())
arr = []

for _ in range(size):
    arr.append(int(sys.stdin.readline()))
arr = arr[::-1]

stack = []
answer = []
for i in range(1, size+1):
    stack.append(i)
    answer.append('+')    

    while stack and stack[-1] == arr[-1]:
        stack.pop()
        arr.pop()
        answer.append('-')

if stack: print('NO')
else:
    for i in answer:
        print(i)

    


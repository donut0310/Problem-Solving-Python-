import sys

lines = int(sys.stdin.readline())

for _ in range(lines):
    string = sys.stdin.readline().split()
    for item in string:
        print(item[::-1],end=' ')
    print(end='\n')
import sys
input = sys.stdin.readline

answer = 0

while True:
    try:
        n = int(input())
    except:
        break
    num = 1

    while True:

        if num % n == 0:
            print(len(str(num)))
            break
        else:
            num = num * 10 + 1




import sys

string = sys.stdin.readline().strip()
arr = []
answer = ''
flag, tmp = 0, ''

for i in string:
    if not flag and i == '<':
        if tmp:
            answer += tmp[::-1]
            answer += i
            tmp = ''
        else: answer += i
        flag = 1
    elif flag:
        if i == '>':
            flag = 0
        answer += i
    else:
        if i == ' ':
            answer += tmp[::-1]
            answer += i
            tmp = ''
        else: tmp += i
    
answer += tmp[::-1]
print(answer)


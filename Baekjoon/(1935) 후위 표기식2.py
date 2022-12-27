import sys,re

def calculate(a, b, exe):
    if exe == '*': return a * b
    elif exe == '/': return b / a
    elif exe == '+': return a + b
    elif exe == '-': return b - a

def solution():
    n = int(sys.stdin.readline())
    string = sys.stdin.readline().strip()
    info = {}

    for ch in string:
        if re.match('[a-zA-Z]', ch):
            info[ch] = 0

    for key in info:
        info[key] = int(sys.stdin.readline())
    
    stack = []
    for ch in string:
        if re.match('[a-zA-Z]', ch):
            stack.append(info[ch])
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(calculate(a, b, ch))

    print(f'{stack[-1]:.2f}')
solution()

'''
ABC*+DE/-
1+2*3-4/5 = 7-0.8 = 6.2
a,(b,c,*) => 6, d,e,/
* => b*c = 6 <= append
+ => a+6 = 7 <= append 
/ => 
- => 
'''
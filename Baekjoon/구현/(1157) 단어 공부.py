import sys
from collections import defaultdict

input = sys.stdin.readline

s = list(input().rstrip().lower())

def solution():
    table = defaultdict(int)

    for ch in s:
        table[ch] += 1
    
    arr = sorted(table.items(), key=lambda x:-x[1])
    
    if len(arr) == 1: return arr[0][0].upper()
    elif arr[0][1] == arr[1][1]: return '?'
    else: return arr[0][0].upper()

print(solution())
from collections import defaultdict
import sys
input = sys.stdin.readline

def is_group_word(word):
    tmp = defaultdict(int)
    
    for i in range(len(word)):
        if i==0: tmp[word[i]] = 1
        else:
            if tmp[word[i]] and word[i-1] != word[i]: return False
            else: tmp[word[i]] = 1
            
    return True

def solution():
    answer = 0
    n = int(input())

    for i in range(n):
        word = input().rstrip()    
        if is_group_word(word): answer += 1

    return answer
print(solution())

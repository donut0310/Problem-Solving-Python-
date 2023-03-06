from collections import defaultdict

def solution(n, m, section):
    answer = 0
    info = defaultdict(int)
    
    for s in section:
        if info[s]: continue
        tmp = s + m
        for i in range(s, tmp):
            info[i] = 1
        answer += 1
        
    return answer
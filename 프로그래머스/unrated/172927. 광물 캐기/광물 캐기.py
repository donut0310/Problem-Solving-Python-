from collections import defaultdict, deque

def solution(picks, minerals):
    answer = 0
    arr = []
    total = sum(picks)
    
    for idx in range(0, len(minerals), 5):
        if total == 0: break
        d, i, s = 0, 0, 0
        total -= 1
        
        for mineral in minerals[idx:idx+5]:
            if mineral == 'diamond': d += 1
            elif mineral == 'iron': i += 1
            else: s += 1
        arr.append((d, i, s))    
    
    arr.sort(key=lambda x:(x[0], x[1], x[2]))

    while arr:
        d, i, s = arr.pop()
        if picks[0]: 
            answer += (d+i+s)
            picks[0] -= 1 
        elif picks[1]: 
            answer += (d*5 + i + s)
            picks[1] -= 1
        elif picks[2]: 
            answer += (d*25 + i*5 + s)
            picks[2] -= 1
        else: break
    return answer
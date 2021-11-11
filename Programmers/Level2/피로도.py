from itertools import permutations

def solution(k, dungeons):
    max_a = 0
    pers = list(permutations(dungeons))
    for p in pers:
        _k = k
        answer=0
        for j in p:
            if _k<j[0]:break
            _k-=j[1]
            answer+=1
        if answer>=max_a: 
            max_a = answer
        if max_a==len(dungeons):
            return max_a
    return max_a

solution(80,[[80,20],[50,40],[30,10]])
# hash
from collections import defaultdict
from itertools import combinations

def solution(clothes):
    dict = defaultdict(list)
    for i in clothes:
        dict[i[1]].append(i[0])

    comb=1
    for i in list(dict.keys()):
        comb*=(len(dict[i])+1)

    return comb-1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
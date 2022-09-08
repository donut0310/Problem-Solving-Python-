from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    
    for cnt in course:
        tmp = defaultdict(int)
        for order in orders:
            comb = combinations(order, cnt)
            for item in comb:
                tmp[''.join(sorted(item))] += 1

        if not len(tmp.keys()): continue
        tmp2 = defaultdict(list)
        for key in tmp:
            tmp2[tmp[key]].append(key)
        max_key = max(sorted(tmp2.keys()))
        if max_key > 1:
            answer.extend(tmp2[max_key])
    answer.sort()
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
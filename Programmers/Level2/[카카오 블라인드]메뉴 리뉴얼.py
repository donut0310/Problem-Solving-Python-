from collections import defaultdict
from itertools import combinations, permutations
def solution(orders, course):
    answer = []
    for i in course:
        tmp=defaultdict(int)
        for j in orders: # 각각의 주문에서 코스 개수로 조합이 가능한 모든 조합을 구한다.
            arr=list(combinations(j,i))
            for k in arr: # 가능한 조합을 dictonary에 카운팅 한다.
                tmp[''.join(sorted(k))]+=1

        modified_tmp = defaultdict(list) # 코스요리: 개수 꼴의 dictionary를 개수: 코스요리 꼴로 바꾼다.
        for l in tmp:
            if tmp[l]>1: # 이때 손님이 2명이상 선택한 메뉴만 추가한다.
                modified_tmp[tmp[l]].append(l)
        if len(modified_tmp)>0: # 만들 수 있는 코스요리가 없으면 새로 추가하지 않는다.
            answer.extend(modified_tmp[max(modified_tmp)])
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))
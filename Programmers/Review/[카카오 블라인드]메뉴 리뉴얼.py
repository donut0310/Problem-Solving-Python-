from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    for cnt in course:
        total = defaultdict(int)
        for order in orders:
            c = combinations(order,cnt)
            for menu in c:
                total[''.join(sorted(menu))]+=1

        new_course = defaultdict(list)
        for menu in total:
            if total[menu]<2: continue
            new_course[total[menu]].append(menu)
        if not len(new_course): continue
        answer.extend(new_course[max(new_course)])
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])) #["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5])) #["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["XYZ", "XWY", "WXA"],[2,3,4])) #["WX", "XY"]

# 풀이 해설
# 코스요리를 구성하는 단품의 개수를(course)를 기준으로
# 각 손님들의 주문내역(orders)의 조합을 구한다. ex) ABC => (AB),(AC),(BA),(BC),(CA),(CB)
# key: 코스요리, value: 주문횟수로 구성된 total 변수에 각 조합을 사전순으로 정렬하여 기록한다
# ex) 'AB':4, 'BC':2, 'CD':2 ...
# key: 횟수, value: 코스요리로 구성된 new_course 변수에 total값을 넣는다.
# 이때 주문횟수가 최소 2 이상인 값들만 넣는다
# ex) 4:['AB'], 2:['BC','CD']
# key 값이 최대인 경우의 코스 요리들이 선택되어야 하기 때문에 조건에 맞게 answer에 넣는다.
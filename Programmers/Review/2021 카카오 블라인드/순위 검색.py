from collections import defaultdict
from itertools import combinations
import re

def bsearch(arr, score):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] >= score: right = mid
        else: left = mid + 1

    return len(arr) - left

def solution(info, query):
    answer = []
    dict = defaultdict(list)

    for item in info:
        cols = item.split(' ')
        score = cols[-1]
        for i in range(5):
            for comb in combinations(cols[:-1], i):
                dict[''.join(comb)].append(int(score))

    for key in dict.keys():
        dict[key].sort()

    for qry in query:
        tmp = ''
        qry = qry.split(' ')
        q = qry[:-1]
        score = int(qry[-1])

        for item in q:
            if item == 'and' or item == '-':
                continue
            tmp +=  item
        if tmp in dict:
            # target = sorted(dict[tmp])
            '''
            27번 줄 코드에서 정렬을 하지 않으면,
            똑같은 쿼리문이 반복 호출 될 때마다 계속 정렬을 해야함
            효율성 테스트 케이스를 만족하지 못하는 주범!!! 
            '''
            target = dict[tmp]

            if len(target):
                answer.append(bsearch(target, score))
        else: answer.append(0)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],\
    ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
# [1,1,1,1,2,4]

from collections import defaultdict
from itertools import combinations
import re

def binary_search(scores,target):
    low,high = 0,len(scores)
    while low<high:
        mid = (low+high)//2
        if scores[mid]>=target:
            high=mid
        else:
            low=mid+1
    return low

def solution(info,query):
    answer=[]
    dict=defaultdict(list)
    # 점수를 제외한 필드의 모든 경우의 수를 구한후 string으로 합쳐서 key로 저장
    # 점수는 해당 key에 value로 저장
    for i in info:
        i=i.split(' ')
        key=i[:-1]
        value=int(i[-1])
        for n in range(5):
            for c in combinations(key,n):
                tmp_key=''.join(c)
                dict[tmp_key].append(value)

    for key in dict.keys():
        dict[key].sort()        

    for q in query:
        q=re.sub(r' and ',' ',q).split(' ')
        target=int(q[-1])
        q=q[:-1]

        while '-' in q:
            q.remove('-')
        tmp=''.join(q)
        if tmp in dict:
            scores = dict[tmp]
            if len(scores)>0:
                answer.append(len(scores)-binary_search(scores,target))
        else: answer.append(0)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
print(solution(["java backend junior pizza 150"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
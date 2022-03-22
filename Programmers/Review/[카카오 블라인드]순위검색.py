from collections import defaultdict

import re
# def binary_search(score_list,score):
#     low,high=0,len(score_list)
#     score_list.sort()
#     while low<high:
#         mid = (low+high)//2
#         if score_list[mid]>=score:
#             high = mid
#         else: low=mid+1
#     return score_list[low:]

# def solution(info, query):
#     answer = []
#     info_dict=defaultdict(list)
#     score_dict=defaultdict(list)
#     [print(i) for i in info]
#     print('---------------------------------')
#     for i in range(len(info)): # 각 컬럼별 딕셔너리 초기화
#         data = info[i].split(' ')
#         for j in range(len(data)):
#             if j==4: score_dict[int(data[j])].append(i)
#             else: info_dict[data[j]].append(i)
#     print(score_dict)
#     for q in query: # 각 쿼리별 info 조사
#         q=re.sub(r' and ',' ',q).split(' ')
#         cnt=len(q) # 확인할 컬럼 개수
#         p_dict = defaultdict(int) # 각 지원자별 확인할 컬럼에 매칭되는 개수 카운팅을 위한 딕셔너리
#         for j in range(len(q)):
#             p_list = []
#             if q[j]=='-':
#                 cnt-=1
#                 continue
#             elif j==4:
#                 arr = binary_search(list(score_dict.keys()),int(q[j]))
#                 [p_list.extend(score_dict[i]) for i in arr]
#             else: 
#                 p_list = info_dict[q[j]]
#             for p in p_list: # 컬럼에 해당되는 응시자의 컬럼 개수 카운팅
#                 p_dict[p]+=1
#         p_cnt=0
#         for i in p_dict.keys():
#             if p_dict[i]==cnt: 
#                 p_cnt+=1
#         answer.append(p_cnt)
#     return answer

# 재풀이 -> 효율성 테스트 만족
from itertools import combinations

def binary_search(scores,target):
    low,high = 0,len(scores)
    while low<high:
        mid = (low+high)//2
        if scores[mid]>=target:
            high=mid
        else: low=mid+1
    return low

def solution(info,query):
    answer=[]
    info_dict=defaultdict(list)
    # 각 info 별 가능한 모든 조합을 구해 딕셔너리에 저장
    for i in info:
        i=i.split(' ')
        tmp = i[:-1]
        value=int(i[-1])
        for cnt in range(5):
            for c in combinations(tmp,cnt):
                info_dict[''.join(c)].append(value)

    #이분탐색을 위한 key별 value 정렬                
    for item in info_dict.keys():
        info_dict[item].sort()

    for q in query:
        q = re.sub(r' and ',' ',q).split(' ')
        while '-' in q:
            q.remove('-')
        key=''.join(q[:-1])
        if key in info_dict.keys():
            scores = info_dict[key]
            target = int(q[-1])
            if len(scores)>0:
                answer.append(len(scores)-binary_search(scores,target))
        else: answer.append(0)
    return answer
# print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
# ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]	))
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
[1,1,1,1,2,4]
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100"]))
# 1
from itertools import combinations
from collections import defaultdict

def solution(relation):
    answer = 0
    index_arr,sub_arr = [],[]

    # relation의 열 개수를 크기로 가지는 index_arr 선언
    [index_arr.append(i) for i in range(len(relation[0]))]

    # relation의 열 번호들의 조합을 가지는 sub_arr 선언
    for i in range(1,len(index_arr)+1):
        sub_arr.extend(combinations(index_arr,i))

    target=[] # 중복되지 않는 row데이터들의 조합정보를 저장(유일성)
    for i in sub_arr:
        tmp_arr=[]
        for r in relation:
            tmp=''
            for j in i: tmp+=r[j]
            tmp_arr.append(tmp)
        if len(tmp_arr)==len(set(tmp_arr)): target.append(i)

    answer = target[::] #값 복사
    for i in range(len(target)-1):
        for j in range(i+1,len(target)):
            tmp = target[i]+target[j] #최소성 만족 검사
            if len(target[j])==len(set(tmp)):
                if target[j] in answer:
                    answer.remove(target[j])
    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]	))

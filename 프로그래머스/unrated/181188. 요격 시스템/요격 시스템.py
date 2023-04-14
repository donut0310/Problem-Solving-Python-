def solution(targets):
    answer = 0
    end = 0
    targets.sort(key=lambda x:(x[1], x[0]))
    
    for s, e in targets:
        if not answer or s >= end:
            answer += 1
            end = e
    return answer

'''
# 그리디 문제
# 백준 (1931) 회의실 배정하기 문제와 유사

1. targets 배열을 폭격 미사일의 종료 지점, 시작 지점 기준으로 정렬한다.
2. 첫 번째 원소는 answer를 1 증가하고, 종료 지점 인덱스를 현재 원소의 종료 지점으로 바꾼다.
3. 다음 원소부터는 다음을 만족한다.
3-1. 폭격 미사일의 시작 지점이 이전 폭격 미사일 종료 지점 인덱스보다 적다면 같은 요격미사일로 격추가 가능하기 때문에 건너뛴다.
3-2. 폭격 미사일의 시작 지점이 이전 폭격 미사일 종료 지점 인덱스보다 크거나 같다면 (개구간 조건)으로 다른 요격 미사일로 격추해야하기 때문에 answer를 1 증가한다.

'''
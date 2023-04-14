import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())

def solution(n:int, arr:list):
    answer = 0
    info = defaultdict(int)
    records = defaultdict(list)
    qualified_team = [0] * (len(set(arr)) + 1)
    rank = []

    # 각 팀마다 결승선 통과 선수 수
    for i in arr:
        info[i] += 1
    
    # 자격있는 팀 선정
    for key, value in info.items():
        if value == 6: qualified_team[key] = 1

    # 점수 배분
    cnt = 1
    for team_number in arr:
        if qualified_team[team_number]: 
            records[team_number].append(cnt)
            cnt += 1

    # 팀 점수 계산
    for team_number, scores in records.items():
        rank.append((team_number, sum(scores[:4]), scores[4]))
    answer = sorted(rank, key=lambda x:(x[1], x[2]))[0][0]

    return answer

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    print(solution(n, arr)) 

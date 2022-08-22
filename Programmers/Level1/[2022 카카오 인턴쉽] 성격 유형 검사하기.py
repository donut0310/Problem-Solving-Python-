'''
1번 지표	라이언형(R), 튜브형(T)
2번 지표	콘형(C), 프로도형(F)
3번 지표	제이지형(J), 무지형(M)
4번 지표	어피치형(A), 네오형(N)

매우 동의나 매우 비동의 선택지를 선택하면 3점을 얻습니다.
동의나 비동의 선택지를 선택하면 2점을 얻습니다.
약간 동의나 약간 비동의 선택지를 선택하면 1점을 얻습니다.
모르겠음 선택지를 선택하면 점수를 얻지 않습니다.

1: 매우 비동의 3
2: 비동의 2
3: 약간 비동의 1
4: 점수 0
5: 약간 동의 1
6: 동의 2
7: 매우 동의 3

'''
from collections import defaultdict

def solution(survey, choices):
    answer = ''
    
    indicators = {
        1: ('R','T'),
        2: ('C','F'),
        3: ('J','M'),
        4: ('A','N')
    }
    
    score_info = {
        1: 3,
        2: 2,
        3: 1,
        4: 0,
        5: 1,
        6: 2,
        7: 3
    }

    user_choice = defaultdict(int)

    for i,v in enumerate(choices):
        char_type = ''
        if v < 4: char_type = list(survey[i])[0]
        elif v > 4: char_type = list(survey[i])[1]
        score = score_info[v]
        user_choice[char_type]+=score
    
    for key,value in indicators.items():
        type_a, type_b = value
        if user_choice[type_a] > user_choice[type_b]: answer += type_a
        elif user_choice[type_a] == user_choice[type_b]: answer += sorted(value)[0]
        else: answer += type_b
    
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])) # TCMA
print(solution(["TR", "RT", "TR"], [7, 1, 3])) # RCJA

'''
<풀이>

1. 성격 지표(indicators)와, 유저 선택에 따른 점수표 socre_info를 각각 딕셔너리로 초기화한다.
2. 유저가 선택한 결과에 따라 성격 유형별 점수를 기록할 user_choice를 defaultdict로 초기화한다.
3. 유저가 선택한 결과 choices를 문제 조건에 맞게 분기하여 점수를 산출하여 user_choice에 점수를 갱신한다.
4. 모든 점수가 기록된 후, 성격 지표(indicators)를 갱신한다.
'''
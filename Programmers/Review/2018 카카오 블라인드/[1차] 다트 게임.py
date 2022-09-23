'''
다트 게임은 총 3번의 기회로 구성된다.
각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
'''
import re

def calculate(score, area, award, score_stack):
    if not len(score_stack): return score

    if area == 'S': score **= 1
    elif area == 'D': score **= 2
    elif area == 'T': score **= 3

    if award == '*':
        score_stack[-1] = score_stack[-1] * 2
        score *= 2
    elif award == '#':
        score = -score

    score_stack.append(score)
    return 

def solution(dartResult):
    answer = 0
    score_stack = [0] # stack
    
    i = 0
    score = 0
    area, award = '', ''
    while i <len(dartResult): 
        if re.match('[0-9]', dartResult[i]):
            calculate(score, area, award, score_stack)
            if dartResult[i+1] == '0': 
                score = 10
                i += 1
            else: 
                score = int(dartResult[i])
            area, award = '', ''
        elif re.match('[SDT]', dartResult[i]):
            area = dartResult[i]
        else: 
            award = dartResult[i]
        i += 1

    calculate(score, area, award, score_stack)
    answer = sum(score_stack)
    return answer

# print(solution("1S2D*3T")) # 37 -> 1^1 * 2 + 2^2 * 2 + 3^3
# print(solution("1D2S#10S")) # 9
# print(solution("1S*2T*3S")) # 23 예제 4 -> 1^1 * 2 * 2 + 2^3 * 2 + 3^1
# print(solution("1D#2S*3S")) # 5 예제 5 -> 1^2 * (-1) * 2 + 2^1 * 2 + 3^1

print(solution("10D")) # 10
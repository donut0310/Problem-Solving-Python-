# 점수: S,D,T => 받은 점수의 1제곱, 2제곱, 3제곱

# 옵션: 스타상, 아차상

# 스타상: 받은 점수 * 2, 이전에 받은 점수 * 2
# 첫번재 점수가 스타상인 경우 => 첫번째 점수만 * 2
# 스타상이 중첩된 경우 => 받은 점수 * 2, 이전에 받은 점수 * 2

# 아차상: 점수 * -1
# 아차상 + 스타상: 아차상을 받은 점수 * 2 => 이미 - 이기 때문에 +2를 곱한다
import re

def parseToString(dartResult):
    return re.findall('[A-Z][#*]*',dartResult)

def parseToNumber(dartResult):
    return re.findall(r'\d+',dartResult)

def bonusScoring(score, bonus, total, i):
    if bonus[i][0] == 'S':
        total[i] = int(score[i])
    elif bonus[i][0] == 'D':
        total[i] = pow(int(score[i]),2)
    elif bonus[i][0] == 'T':
        total[i] = pow(int(score[i]),3)
    return total

def optScoring(bonus, total, i):
    if bonus[i][1] == '#': # 아차상인 경우
        total[i] *= -1
    elif bonus[i][1] == '*': # 스타상인 경우
        if i==0: # 첫번째 점수가 스타상인 경우
            total[i] *= 2
        elif i!=0 and len(bonus[i-1]) == 2 and bonus[i-1][1] =='#': # 스타상 이전에 아차상인 경우
            total[i-1] *= 2
            total[i] *= 2
        elif i!=0 and len(bonus[i-1]) == 2 and bonus[i-1][1]=='*': # 스타상이 중첩된 경우
            total[i-1] *= 2
            total[i] *= 2
        else:
            total[i-1] *= 2
            total[i] *= 2
    return total
    
def scoring(score,bonus,total):
    for i in range(len(bonus)):
        total = bonusScoring(score,bonus,total,i)
        if len(bonus[i]) == 2: # 옵션이 있는 경우
            total = optScoring(bonus,total,i)
    return total

def solution(dartResult):
    score,bonus,total = [],[],[0,0,0]
    answer = 0

    score = parseToNumber(dartResult)   
    bonus = parseToString(dartResult)   
    total = scoring(score,bonus,total)
    answer = sum(total)
    return answer

# solution('1S2D*3T')
# solution('1D2S#10S')
# solution('1D2S0T')
# solution('1S*2T*3S')
# solution('1D#2S*3S')
# solution('1T2D3D#')
# solution('1D2S3T*')
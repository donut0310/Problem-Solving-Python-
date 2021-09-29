# Brute Force
def compare(brown,yellow,vertical,horizon):
    if (vertical+2)*(horizon+2)==brown+yellow:
        return True
    return False

def divisor(brown,yellow):
    horizon,vertical=0,0
    for i in range(1,yellow+1):
        if yellow%i==0 and i<=yellow//i:
            vertical,horizon=i,yellow//i
            if compare(brown,yellow,vertical,horizon):
                return horizon,vertical
    return 0,0

def solution(brown, yellow):
    answer = []
    horizon, vertical = divisor(brown,yellow)

    answer.extend([horizon+2,vertical+2])
    return answer

# solution(10,2)
# solution(8,1)
solution(14,4)
# solution(24,24)

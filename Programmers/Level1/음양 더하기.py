def realNumber(absolutes,signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]==False:
            answer+= absolutes[i]*-1
        else: answer += absolutes[i]
    return answer

def solution(absolutes, signs):
    answer = realNumber(absolutes,signs)
    return answer

solution([4,7,12],[True,False,True])
solution([1,2,3],[False,False,True])
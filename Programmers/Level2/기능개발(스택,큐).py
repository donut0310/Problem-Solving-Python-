from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    date = [math.ceil((100-p)/s) for (p,s) in zip (progresses,speeds)]        

    while len(date)!=0:
        i = 0
        cnt = 0
        for i in range(len(date)):  
            if date[i]-date[0]>0:
                break
            else:
                cnt+=1
        date = date[cnt:]
        answer.append(cnt)
    return answer

solution([93,30,55],[1,30,5])
solution([95,90,99,99,80,99],[1,1,1,1,1,1])
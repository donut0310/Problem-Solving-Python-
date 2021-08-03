from collections import deque
import math
from typing import get_origin

def shortest(fingerLocation,target):
    graph = {
        0:[[8,11,12],math.inf],
        1:[[2,4],math.inf],
        2:[[1,3,5],math.inf],
        3:[[2,6],math.inf],
        4:[[1,5,7],math.inf],
        5:[[2,4,6,8],math.inf],
        6:[[3,5,9],math.inf],
        7:[[4,8,11],math.inf],
        8:[[5,7,9,0],math.inf],
        9:[[6,8,12],math.inf],
        11:[[7,0],math.inf],
        12:[[0,9],math.inf]
    }
    visited = []
    visit_cnt=0
    
    s_v=fingerLocation
    graph[s_v][1]=0
    visited.append(s_v)
    queue = deque(graph[s_v][0])
    while queue:
        visit_cnt+=1
        cnt = len(graph[s_v][0])
        while cnt>0:
            n=queue.popleft()
            if n not in visited:
                visited.append(n)
                queue.extend(graph[n][0])
                if graph[n][1]>graph[s_v][1]:
                    graph[n][1]=graph[s_v][1]+1
            if n==target:
                return graph[n][1]
            cnt-=1
        s_v=visited[visit_cnt]

def solution(numbers,hand):
    answer=''
    leftPoint = 10 # *
    rightPoint = 12 # #

    for i in numbers:
        newStr=[]
        if i in (1,4,7):
            newStr.append('L')
            leftPoint = i
        elif i in (3,6,9):
            newStr.append('R')
            rightPoint = i
        else:
            ls = shortest(leftPoint,i)
            rs = shortest(rightPoint,i)
            if ls==rs:
                if hand=='right':
                    newStr.append('R')
                    rightPoint=i
                else:
                    newStr.append('L')
                    leftPoint=i
            elif ls<rs:
                newStr.append('L')
                leftPoint=i
            else:
                newStr.append('R')
                rightPoint=i
        answer+=''.join(newStr)
    print('answer:',answer)
    return answer

solution([1,3,4,5,8,2,1,4,5,9,5],'right')
solution([7,0,8,2,8,3,1,5,7,6,2],'left')
solution([1,2,3,4,5,6,7,8,9,0],'right')
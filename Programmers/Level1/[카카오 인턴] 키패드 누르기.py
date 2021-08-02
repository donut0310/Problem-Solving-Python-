def getDistance(fingerPoint,index):
    keypad={
        0:{'x':1,'y':0},
        1:{'x':0,'y':3},
        2:{'x':1,'y':3},
        3:{'x':2,'y':3},
        4:{'x':0,'y':2},
        5:{'x':1,'y':2},
        6:{'x':2,'y':2},
        7:{'x':0,'y':1},
        8:{'x':1,'y':1},
        9:{'x':2,'y':1},
        10:{'x':0,'y':0},
        11:{'x':2,'y':0},
    }
    return abs(keypad[fingerPoint]['x']-keypad[index]['x']) + abs(keypad[fingerPoint]['y']-keypad[index]['y'])

def judgement(ls,rs,hand,leftPoint,rightPoint,i):
    newStr = []
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
    return newStr,leftPoint,rightPoint

def solution(numbers,hand):
    answer=''

    leftPoint = 10
    rightPoint = 11

    for i in numbers:
        newStr=[]
        if i in (1,4,7):
            newStr.append('L')
            leftPoint = i
        elif i in (3,6,9):
            newStr.append('R')
            rightPoint = i
        else:
            ls = getDistance(leftPoint,i)
            rs = getDistance(rightPoint,i)
            newStr,leftPoint,rightPoint = judgement(ls,rs,hand,leftPoint,rightPoint,i)
        answer += ''.join(newStr)
    return answer
# solution([1,3,4,5,8,2,1,4,5,9,5],'right')
# solution([7,0,8,2,8,3,1,5,7,6,2],'left')
# solution([1,2,3,4,5,6,7,8,9,0],'right')


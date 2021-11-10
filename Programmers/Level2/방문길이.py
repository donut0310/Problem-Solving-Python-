from collections import defaultdict

def solution(dirs):
    start = (5,5)
    visited = set()

    dx = {'U':0,'D':0,'L':-1,'R':1}
    dy = {'U':-1,'D':1,'L':0,'R':0}

    for i in dirs:
        a = (start[0]+dx[i],start[1]+dy[i])
        if 0<=a[0]<=10 and 0<=a[1]<=10:
            visited.add(tuple(sorted([start,a])))
            start = (a[0],a[1])
    return len(visited)

# solution('ULURRDLLU') 
# solution('LULLLLLLU')
solution('LLLLRLRLRLL')

from collections import deque
def solution(numbers, target):
    answer1,answer2 = 0,0
    q1,q2 = deque(),deque()
    q1.append((0,answer1))
    q2.append((0,answer2))
    arr1,arr2=[numbers[0]],[-1*numbers[0]]

    for i in range(1,len(numbers)):
        for j in range(2**(i)):
            if j%2==0:
                arr1.append(-1*numbers[i])
                arr2.append(-1*numbers[i])
            else:
                arr1.append(numbers[i])
                arr2.append(numbers[i])
    map1 = [0*i for i in range(0,2**(len(numbers))-1)]
    map2 = [0*i for i in range(0,2**(len(numbers))-1)]
    while q1:
        start,answer=q1.popleft()
        answer1=answer+arr1[start]
        map1[start]=answer1
        for i in range(1,3): #2갈래 조사
            if start*2+i<len(arr1):
                q1.append((start*2+i,answer1))
    map1 = map1[len(map1)-(2**(len(numbers)-1)):]

    while q2:
        start,answer=q2.popleft()
        answer2=answer+arr2[start]
        map2[start]=answer2
        for i in range(1,3): #2갈래 조사
            if start*2+i<len(arr2):
                q2.append((start*2+i,answer2))
    map2 = map2[len(map2)-(2**(len(numbers)-1)):]
    return map1.count(target)+map2.count(target)

# solution([1,1,1,1,1],3)
print(solution([2,3,5,7,9],2))
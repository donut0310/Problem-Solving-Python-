from collections import deque

def binaryScale(n,arr):
    for i in range(len(arr)):
        queue = deque()
        tmp=arr[i]
        while tmp>=2:
            queue.appendleft(tmp%2)
            tmp//=2
        queue.appendleft(tmp)
        if len(queue)!=n:
            for j in range(n-len(queue)):
                queue.appendleft(0)
        arr[i] = queue
    return arr

def mapping(n,arr1,arr2):
    answer = []
    for i in range(n):
        string = ''
        for j in range(n):
            if arr1[i][j] == 0 and arr2[i][j]==0:
                string += ''.join(' ')
            else:
                string += ''.join('#')
        answer.append(string)
    return answer

def solution(n, arr1, arr2):
    answer = []
    arr1 = binaryScale(n,arr1)
    arr2 = binaryScale(n,arr2)
    answer = mapping(n,arr1,arr2)
    return answer

solution(5,[9,20,28,18,11],[30,1,21,17,28])
solution(6,[46,33,33,22,31,50],[27,56,19,14,14,10])
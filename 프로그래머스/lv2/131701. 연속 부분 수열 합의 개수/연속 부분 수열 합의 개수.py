from collections import deque

def solution(elements):
    answer = 0
    arr = []
    size = len(elements)
    tmp = [0] * size
    
    for i in range(size):
        if i > 0: elements.append(elements[i-1])
        
        for j in range(i, size + i):
            tmp[j-i] += elements[j]
            
        arr.extend(tmp)
        
    answer = len(set(arr))
    return answer

'''
<풀이>
원형 수열이기 때문에 부분 수열의 합을 구하려면 원래 배열의 맨 앞 인덱스부터 만들려는 부분 수열의 길이까지의 인덱스를 원래 배열의 뒤에 붙여줘야 한다.
만들 수 있는 부분 수열의 길이는 1~원래 배열의 사이즈 만큼 만들 수 있으며,
각 부분 수열에 포함되는 원소의 개수는 원래 배열의 사이즈와 같다.(중복 미포함시)

그렇기 때문에 반복문의 각 스테이지마다 tmp 배열에 부분수열의 원소들을 저장하고
이전 스테이지에서 만들어진 tmp 배열에 같은 인덱스에 위치한 원소 값에 누적합을 구한다면
보다 빠르게 합을 구할 수 있다.
ex) 
원래 부분 수열 [7,9,1,1,4]
stage 0: 
    원형 수열 = 원래 부분 수열 => [7,9,1,1,4]
    부분 수열 = [7, 9, 1, 1, 4]
stage 1: 
    원형 수열 = 원래 부분 수열 + 원래 부분 수열[stage-1] => [7,9,1,1,4,7]
    부분 수열 = [(7+9), (9+1), (1+1), (1+4), (4+7)]
stage 2:
    원형 수열 = 원래 부분 수열 + 원래 부분 수열[stage-1] => [7,9,1,1,4,7,9]
    부분 수열 = [(7+9+1), (9+1+1), (1+1+4), (1+4+7), (4+7+9)]
    .
    .
    .
'''
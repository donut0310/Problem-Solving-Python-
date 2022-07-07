import heapq
def solution(n, works):
    answer = 0
    arr = [-i for i in works]
    heapq.heapify(arr)

    while n>0 and arr:
        tmp = heapq.heappop(arr)+1
        if tmp!=0: heapq.heappush(arr,tmp)
        n-=1
    for i in arr:
        answer+=i**2
    return answer

print(solution(4,[4,3,3]))
print(solution(1,[2,1,2]))
print(solution(3,[1,1]))

'''
<풀이>
제곱수의 성질을 봤을때, 1^2 = 1, 2^2 = 4, 3^3 = 9 ... 99^99 = 9801, 100^100 = 10000로 수가 클수록 제곱수끼리의 차이는 엄청 커진다.
따라서, 당장의 작업량이 가장 큰 작업을 최소로 줄이는게 아닌, 모든 작업량들 중 가장 큰 작업량을 -1씩 감소해야한다.
매 반복마다 최대값을 -1 시키기 위해 힙 자료구조를 사용하여, 최대힙을 통해 최대값을 업데이트한다.
'''
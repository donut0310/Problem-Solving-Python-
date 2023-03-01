import heapq

def solution(n, k, enemy):
    answer = 0
    arr = []
    for idx, i in enumerate(enemy):
        heapq.heappush(arr, -i)
        if k == 0 and n < i: break
        if n < i:
            k -= 1
            n += -arr[0]
            heapq.heappop(arr)
        n -= i
        answer += 1

    return answer

'''
<풀이>

각 라운드에 무조건 n(병사) - i(적) 연산을 진행한다.
만일 n이 i보다 작다면 해당 라운드는 이길 수 없기 때문에 무적권을 사용해 넘겨야 한다.
이때, 이미 지나온 라운드 중에서 가장 적의 수가 많은 라운드에 무적권을 적용하면 
해당 라운드에서 소모된 병사 수가 다시 회복되기 때문에 현재 라운드를 이길 수 있게된다.
가장 적의 수가 많은 라운드는 최대힙을 활용해서 구할 수 있다.
'''
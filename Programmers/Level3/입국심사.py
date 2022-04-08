def solution(n,times):
    #심사시간이 가장 바른 심사관이 모든 사람을 검사할 때가 최소시간의 최대치이다.
    left, right = 1, n*min(times) 
    #이분 탐색
    while left<=right:
        mid = (left+right)//2 
        p = 0 # 심사를 받은 사람의 수
        for t in times:
            p += mid//t # 각 심사관이 심사한 사람들의 수를 카운팅
            if p>=n: # 입국심사가 완료된 사람의 수가 n보다 크거나 같다면 => 더 적은 시간에 처리할 수 있음을 의미
                right = mid-1
                answer = mid
                break
        if p<n: # 입국심사가 완료된 사람의 수가 n보다 작다면 => 시간이 부족함을 의미
            left=mid+1
    return answer

print(solution(6,[7,10]))

'''
<풀이>
심사를 받는데 걸리는 시간의 최솟값을 구하라 => 시간을 기준으로 이분탐색
1. 이분탐색의 left,right 선언: left = 최소시간 1분, right = 최대시간 => 가장 심사시간이 짧은 심사관이 모든 사람을 심사했을 때의 시간 n*min(times)
2. for loop를 통해 정해진 시간(mid)내에 각 심사관이 처리할 수 있는 사람의 수를 구해 p에 카운팅 해준다.
3. p값이 n(입국심사를 기다리는 사람)보다 크거나 같다면 mid보다 더 적은 시간에 심사가 완료될 수 있음을 의미한다.
3-1. right값을 mid-1로 변경해주고 이때의 mid값을 answer에 저장해주고 for loop를 탈출한다.
4. p값이 n보다 작다면 mid값이 부족하다 -> 시간이 부족함을 의미하기에 left값을 mid+1로 변경해준다.
'''

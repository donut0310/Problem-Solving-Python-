from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    info = defaultdict(int)
    
    for i in tangerine:
        info[i] += 1
    arr = sorted(info.items(), key = lambda x:-x[1])

    for t, cnt in arr:
        answer += 1
        if k <= cnt:
            break
        k -= cnt
        
    return answer

'''
<풀이>
주어진 귤의 종류와 각 종류별 개수들로 k 값을 만들기 위한 최소 종류의 집합을 구하기 위해선
종류별 개수를 카운팅해야한다 -> dictionary 이용

위에서 구한 dictionary는 key 귤의 종류: value 귤의 개수로 이루어지며 
value를 기준으로 내림차순 정렬을 한다.

가장 많은 개수를 가진 귤의 종류부터 반복문을 이용해 k 값을 감소하고
k 값이 0보다 작거나 같은 경우가 최소 종류의 귤을 담았을 때를 보장하게된다.
'''
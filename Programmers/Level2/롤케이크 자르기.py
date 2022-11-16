from collections import defaultdict

def solution(topping):
    answer = 0
    older, younger = defaultdict(int), defaultdict(int)
    o_cnt, y_cnt = len(set(topping)), 0

    for t in topping: # 형이 가지고 있는 토핑들 초기화
        older[t] += 1
    
    while y_cnt <= o_cnt:
        t = topping.pop()
        # 형이 토핑을 두 개 이상 가지고 있다면 -1
        # 형이 토핑을 한 개 가지고 있다면 가지고 있는 토핑 종류에서 해당 토핑을 제거
        if older[t] > 1: older[t] -= 1
        else: 
            del older[t]
            o_cnt -= 1
        
        # 동생이 가지고 있는 토핑 종류 갱신
        if not younger[t]: 
            younger[t] += 1
            y_cnt += 1
        
        # 형이 가지고 있는 토핑의 종류와 동생이 가지고 있는 토핑의 종류가 같다면 answer += 1
        if o_cnt == y_cnt: answer += 1   
    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2])) # 2
# print(solution([1, 2, 3, 1, 4])) # 

'''
<풀이>
형이 모든 토핑을 가지고 있다고 가정하고 시작
형이 가지고 있는 토핑의 종류별 개수를 딕셔너리에 저장한다 -> older
동생도 마찬가지로 딕셔너리에 저장하지만 빈값이다 -> younger

1. 맨 뒤의 토핑부터 배열에서 빼내면서 조건에 맞게 older, younger 딕셔너리를 갱신한다.
2. 형이 가지고 있는 토핑의 종류(o_cnt)가 더 많게 시작했기 때문에 o_cnt >= y_cnt를 만족할 때까지 1의 과정을 반복한다.
'''
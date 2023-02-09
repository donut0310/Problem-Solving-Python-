from collections import defaultdict
from itertools import combinations

def get_gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def get_lcm(a,b):
    if a < b: return a * b // get_gcd(b, a)
    else: return a * b // get_gcd(a, b)

def solution(weights):
    answer = 0
    set_weights = set()
    w_dict = defaultdict(int)
        
    for weight in weights:
        w_dict[weight] += 1
        set_weights.add(weight)
    
    # 같은 무게의 경우 nC2
    for key in w_dict:
        if w_dict[key] > 1: answer += w_dict[key] * (w_dict[key] - 1) // 2
    
    # 다른 무게들의 경우
    for p1, p2 in combinations(set_weights, 2):
        lcm = get_lcm(p1, p2)
        min_limit = max(p1, p2) * 2
        max_limit = min(p1, p2) * 4
        pair = 0
        
        for i in range(1, 4):
            tmp = lcm * i
            if tmp < min_limit: continue
            elif tmp > max_limit: break
            else: pair += 1
        
        answer += w_dict[p1] * w_dict[p2] * pair

    return answer

'''
<풀이>
1. 동일한 무게의 사람이 존재할 수 있기 때문에 w_dict로 중복을 카운팅한다. 
2. 같은 무게의 사람끼리는 거리에 상관없이 시소의 평형이 이루어진다. 즉, 모든 경우의 수는 nC2를 만족
    => answer += w_dict[p] * (w_dict[p]-1) // 2
3. 다른 무게의 사람끼리는 본인의 무게 * 시소 중심까지의 거리가 같을 때 시소의 평형이 이루어진다.
3-1. 다른 무게의 사람끼리의 모든 조합을 구한다.
3-2. 조합마다 최소 공배수를 구하는데 이때 최소 공배수의 범위는 '둘 중 무거운 사람의 2m에서의 무게 ~ 둘 중 가벼운 사람의 4m에서의 무게'에 속해야한다.
3-3. 해당 범위에 속할 때 두 사람이 이룰 수 있는 시소의 평형 쌍(pair)을 1 증가한다.
3-4. 중복조합이 가능하기 때문에 아래 식을 적용한다.
    => answer += w_dict[사람1] * w_dict[사람2] * pair
'''
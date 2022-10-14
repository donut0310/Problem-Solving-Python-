from collections import defaultdict

def solution(clothes):
    answer = 0
    c_dict = defaultdict(int)
    
    for v,k in clothes:
        c_dict[k] += 1
    
    x = 1
    for value in c_dict.values():
        x *= (value+1)
    x -= 1
    answer = x
    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])) # 5

'''
n차식 계수 이용
a: 2
b: 3
c: 3 의 경우일 때,
모든 경우의 수는 a + b + c + ab + ac + bc + abc가 된다.
이는 3차식의 계수의 합과 동일하다 => x^3 + (a+b+c)x^2 + (ab+bc+ca)x + abc == (x+a)(x+b)(x+c)
이는 옷의 종류가 3개라면 전체 경우의 수는 3차식의 계수의 합에 해당하고, 옷의 종류가 n개라면 n차식의 계수의 합에 해당하는것을 의미한다.

위 계수의 총합은 x에 1을 대입한 후 x^3의 값(1) 을 빼면 된다.

따라서, (x+a)(x+b)...(x+n)의 식을 적용하면된다.

'''
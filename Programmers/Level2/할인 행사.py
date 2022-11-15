from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    info = defaultdict(int)

    for item in discount:
        info[item] += 1

    for item in want:
        if not info[item]: return 0

    days = sum(number)
    for i in range(len(discount) - days + 1):
        tmp = defaultdict(int)
        flag = 0
        for j in range(i, i+10):
            tmp[discount[j]] += 1

        for j in range(len(want)):
            if number[j] != tmp[want[j]]:
                flag = 1
                break
        if not flag: answer += 1
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
# 3

'''
<풀이>
1. 구매할 전체 개수 sum(number)을 for loop의 증감 수치로 사용한다.
2-1. discount의 i ~ i+sum(number) 사이의 품목들을 tmp 딕셔너리에 추가한다.
2-2. tmp딕셔너리에 담긴 구매할 품목들의 개수가 number에서의 품목의 개수와 일치하는지 비교한다.
'''

'''
다른 방법으로 개선해볼 필요가 있다.
'''
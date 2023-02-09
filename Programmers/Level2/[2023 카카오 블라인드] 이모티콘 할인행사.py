from itertools import product

def solution(users, emoticons):
    answer = []

    p = list(product(([10, 20, 30, 40]), repeat=len(emoticons)))
    
    for rate_info in p:
        plus_service = 0
        total_amount = 0

        for user_rate, user_limit in users:
            tmp_amount = 0
            
            for i in range(len(rate_info)):
                emoticon_rate = rate_info[i]
                
                if user_rate <= emoticon_rate: tmp_amount += emoticons[i] * (100 - emoticon_rate) // 100
            if tmp_amount >= user_limit: plus_service += 1
            else: total_amount += tmp_amount

        answer.append((plus_service, total_amount))
    
    answer.sort(key = lambda x:(-x[0], -x[1]))
    return answer[0]

'''
각 이모티콘 할인율 10%, 20%, 30%, 40% 중 하나
이모티콘의 종류는 최대 7개

1. 이모티콘 개수 만큼 적용 가능한 할인율 경우의 수 구하기
2. 사용자 별 이모티콘의 할인된 금액의 총 합이 본인의 가격보다 크다면 이모티콘 플러스 가입, 작다면 이모티콘 구매
'''

print(solution([[40, 10000], [25, 10000]], [7000, 9000])) # [1, 5400]
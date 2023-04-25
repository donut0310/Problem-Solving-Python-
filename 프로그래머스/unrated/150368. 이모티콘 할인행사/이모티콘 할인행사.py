from itertools import product

def solution(users, emoticons):
    answer = []
    
    # 할인율 경우의 수 => 곱집합
    rate_info = list(product([10, 20, 30, 40], repeat=len(emoticons)))
    
    '''
    1. 각 할인율 경우의 수 마다 유저가 원하는 할인율과 비교
    2. 유저가 원하는 할인율 이상인 경우 tmp_price를 갱신한다.
    3. tmp_price 가 유저의 한도 금액보다 크거나 같다면 플러스 유저 가입 수를 +1하고 더 이상의 이모티콘 구매를 진행하지 않는다.
    4. 각 할인율 경우의 수마다 (플러스 서비스 가입 수, 플러스 서비스 미가입자들의 이모티콘 구매 합계)를 answer에 저장한다.
    '''
    for info in rate_info:
        plus_user = 0
        total_price = 0
        
        for user_rate, user_amount in users:
            tmp, flag = 0, 0
            
            for i, rate in enumerate(info):        
                if user_rate <= rate:
                    tmp += emoticons[i] * (100-rate) // 100
                    
                if tmp >= user_amount:
                    plus_user += 1
                    flag = 1
                    break
                    
            if not flag: total_price += tmp
        answer.append((plus_user, total_price))
    
    answer.sort(key=lambda x:(-x[0], -x[1]))
    answer = answer[0]
    return answer
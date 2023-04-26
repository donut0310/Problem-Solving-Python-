from collections import defaultdict

def calculation(info, person, amount):
    info[person][0] += amount
    return

def dfs(info, seller, amount):
    if seller == '-':
        calculation(info, seller, amount) 
        return
    
    tmp = amount // 10
    # 추천인에게 이익금 배분
    if tmp >= 1:
        # 재귀 -> 상위 추천인에게 이익금 배분
        recommender = info[seller][1]
        dfs(info, recommender, tmp)
    else: 
        calculation(info, seller, amount)
        return
    
    calculation(info, seller, amount - tmp)
    return
    
    
def solution(enroll, referral, seller, amount):
    answer = []
    
    info = defaultdict(list)
    
    # 사원, 추천인 딕셔너리 초기화
    for i in range(len(enroll)):
        info[enroll[i]] = [0, referral[i]]
        
    info['-'] = [0, '']
    
    # 판매자, 판매량 정보를 가지고 상위 노드로 이익금 배분을 재귀로 구현
    for i in range(len(seller)):
        dfs(info, seller[i], amount[i] * 100)
    
    # 집계
    for person in enroll:
        answer.append(info[person][0])
        
    return answer



'''
enroll => 판매원의 이름
referral => 추천인의 이름
enroll과 referral은 1:1 매치

seller => 판매자
amount => 판매량 
seller와 amount는 1:1 매치

key = enroll, value = (cost, referral) 딕셔너리 초기화
for loop -> seller, amount
    dfs()
'''
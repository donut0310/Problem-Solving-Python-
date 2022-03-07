from collections import defaultdict

def recur(someone,profit_tree,tree,amount):
    self_own = amount-amount//10
    dist = amount//10
    if someone=='center' or dist<1: 
        profit_tree[someone]+=self_own
        return profit_tree
    profit_tree[someone]+=self_own
    recur(tree[someone],profit_tree,tree,dist)
    return profit_tree

def solution(enroll, referral, seller, amount):
    answer = []
    tree = defaultdict(str)
    profit_tree = defaultdict(int)

    for i in range(len(referral)):
        if referral[i]=='-':
            tree[enroll[i]]='center'
        else: tree[enroll[i]]=referral[i]

    for i in range(len(seller)):
        profit_tree=recur(seller[i],profit_tree,tree,amount[i]*100)

    for i in enroll:
        answer.append(profit_tree[i])
    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]))
#[360, 958, 108, 0, 450, 18, 180, 1080]

# 수익금 분배구조를 round(amount*0.9)로 구현시 전체 테케가 오답
# amount-amount//10 으로 변경시 정답 처리
# round 처리시 반올림에 의해 문제에서 의도한 대로의 값이 부정확해지는 경우가 발생!
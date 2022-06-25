from collections import defaultdict
from itertools import permutations

def check(id, target):
    if id.count('*') == len(id): return True # 불량 사용자의 아이디가 모두 '*' 로 이루어진 경우 True 반환
    for i in range(len(id)):
        if id[i]=='*': continue
        if id[i]!=target[i]: return False # 한 글자라도 다른 경우 False 반환
    return True

def solution(user_id, banned_id):
    banned_dict = defaultdict(list) # 불량 사용자의 아이디 형태와 같은 사용자 아이디 매핑 'user_id':['banned_id1','banned_id2']
    candidates = set() # 불량 사용자 아이디 형태와 같은 사용자 아이디 후보군
    for id in banned_id:
        for target in user_id:
            if len(id) == len(target) and check(id,target): # 불량 사용자의 아이디 형태와 일치하는 경우
                banned_dict[target].append(id)
                candidates.add(target)
    p = list(permutations(list(candidates),len(banned_id))) # 후보군 순열 

    check_dict = defaultdict(int) # 불량 사용자 아이디의 포매소가 일치하는 후보군 리스트를 키로 가지는 dict
    for items in p:
        # check format
        flag=0
        for i in range(len(items)):
            if banned_id[i] not in banned_dict[items[i]]:
                flag = 1
                break
        # check duplicated
        if flag: continue
        tmp = ''.join(sorted(items))
        if tmp not in check_dict:
            check_dict[tmp]+=1

    return len(check_dict)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])) # 3

'''
<풀이>

'''
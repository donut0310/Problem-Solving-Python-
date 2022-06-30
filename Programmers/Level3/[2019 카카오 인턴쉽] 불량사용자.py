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

    check_dict = defaultdict(int) # 불량 사용자 아이디의 포맷이 일치하는 후보군 리스트를 키로 가지는 dict
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
1. 불량 사용자 아이디(banned_id)의 후보군이 될 수 있는 유저 아이디(user_id)를 banned_dict에 저장 => 'user_id':['banned_id1','banned_id2']
2. 후보군이 되는 사용자 아이디를 candidated 집합체에 추가
3. candidated 집합체에 대해서 순열을 구함
4. 순열의 각 조합으로 banned_id와 포맷이 같은지 조사 후 같지 않다면 스킵
5. 4에서 스킵이 되지 않은 경우, 해당 조합을 사전순으로 정렬한 문자열을 key로 check_dict에 추가
6. 이때, 이미 존재하는 경우 중복이므로 스킵
7. check_dict의 개수를 반환하고 종료
'''
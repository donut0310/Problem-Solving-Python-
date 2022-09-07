from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    user_info = defaultdict(int)
    target_info = defaultdict(list)
    duplicate = set()
    for record in report:
        if record in duplicate: continue
        duplicate.add(record)
        user, target_user = record.split(' ')
        target_info[target_user].append(user)

    for target in target_info:
        p = target_info[target]
        if len(p) >= k:
            for i in p:
                user_info[i]+=1
    
    for user in id_list:
        answer.append(user_info[user])
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)) # [2, 1, 1, 0]
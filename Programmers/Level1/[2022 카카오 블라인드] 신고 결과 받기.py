from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    target_list = set()
    users = {} # user: {set{target user}, set{user who reports}}

    for i in id_list:
        users[i]=[set(), set()]

    for i in report:
        user, target = i.split(' ')
        users[user][0].add(target)
        users[target][1].add(user)
        if len(users[target][1])>=k:
            target_list.add(target)
    
    for i in users:
        answer.append(len(set(target_list & users[i][0])))
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
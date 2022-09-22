from collections import defaultdict

def solution(record):
    answer = []
    users = defaultdict(str)
    
    for i in record:
        s = i.split(' ')
        if len(s) > 2: users[s[1]] = s[2]

    for i in record:
        s = i.split(' ')
        if s[0] == 'Change': continue
        if len(s) == 2: answer.append(f'{users[s[1]]}님이 나갔습니다.')
        else: answer.append(f'{users[s[1]]}님이 들어왔습니다.')

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

from collections import defaultdict

def solution(record):
    answer = []
    users = defaultdict(str)    
    
    # users 정보 초기화
    for i in record:
        user = i.split(' ')
        if len(user) == 2: continue # Leave
        users[user[1]] = user[2] # Enter, Change
    
    # answer에 유저 변동 정보 저장
    for i in record:
        user = i.split(' ')
        if user[0] == 'Change': continue
        if len(user) == 2: answer.append(f'{users[user[1]]}님이 나갔습니다.')
        else: answer.append(f'{users[user[1]]}님이 들어왔습니다.')

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

# key: 유저 아이디, value: 유저 닉네임을 값으로 가지는 users:{} 딕셔너리를 구성한 후
# 각 record 별로 유저의 변동된 정보를 저장한다.
# 이후 각 record 별로 최신화 된 유저의 정보를 대입해 answer 값을 결정한다.

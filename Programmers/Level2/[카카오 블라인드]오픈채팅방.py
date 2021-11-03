def solution(record):
    result = []
    answer=[]
    user_dict = {}

    for i in record:
        r = i.split(' ')
        status = r[0]
        user = r[1]
        if status=='Enter':
            nickname=r[2]
            user_dict[f'{user}'] = nickname 
            result.append(f'{user}님이 들어왔습니다.')
        elif status=='Leave':
            result.append(f'{user}님이 나갔습니다.')
        elif status=='Change':
            nickname=r[2]
            user_dict[f'{user}']=nickname
    for i in range(len(result)):
        past_name = result[i].split('님이')[0]
        result[i] = result[i].replace(past_name,user_dict[f'{past_name}'])
    return result

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
import re

def solution(new_id):
    answer = ''
    # 1 
    new_id = new_id.lower()
    # 2
    new_id = re.sub('[^\.a-z0-9-_]', '' , new_id)
    # 3
    new_id = re.sub('\.+', '.', new_id)
    # 4
    new_id = new_id.strip('.')
    # 5
    if not new_id: new_id += 'a'
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip('.')
    # 7
    if len(new_id) <= 2:
        tmp = new_id[-1]
        while len(new_id) < 3:
            new_id += tmp

    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm")) # "bat.y.abcdefghi"

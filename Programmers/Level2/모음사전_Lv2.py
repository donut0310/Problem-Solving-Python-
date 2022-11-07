def solution(word):
    answer = 0
    _str, cnt = '', 0
    order = { 'A':'E', 'E':'I', 'I':'O', 'O':'U'}
    
    while _str != word and _str != 'UUUUU':
        cnt += 1
        if len(_str) != 5:
            _str += 'A'
        elif _str[-1] == 'U':
            u_cnt = 0
            for i in range(4, -1, -1):
                if _str[i] == 'U': u_cnt += 1
                else: break
            tmp = _str[i]
            _str = _str[:i]
            _str += order[tmp]
        else:
            tmp = _str[-1]
            _str = _str[:4] + order[tmp]

    answer = cnt
    return answer

print(solution("AAAAE")) # 6
print(solution("AAAE")) # 10
print(solution("I")) # 1563
print(solution("EIO")) # 1189

''' 
<풀이>
1. 5 글자가 될 때까지 'A' 추가
2. 마지막 글자가 'U'가 되면 _str 문자열의 뒤에서부터 'U'가 안나올 때까지 개수(u_cnt)를 센다.
2-1. 이후 'U'가 아닌 글자를 만나면 해당 글자를 tmp 변수에 담고, u_cnt-1 까지의 글자를 모두 없애준다.
2-2. 바뀐 _str 글자의 마지막 글자에 2-1과정에서 만든 tmp 변수의 다음 모음값을 추가한다.
3. _str 문자열이 5글자가 되면 마지막 글자의 값은 다음 모음값으로 바꿔준다.
4. 위 과정을 _str 값이 word 갑이 되거나 사전의 마지막 글자 ('UUUUU') 가 될 떄까지 반복한다.
'''

def solution(s, n):
    answer = ''
    
    for i in s:
        print(i)
        if i == ' ':
            answer+=''.join(' ')
            continue
        elif i >= 'a' and i <= 'z':
            i = ord(i)+n
            if i > ord('z'):
                i -= 26
        elif i >= 'A' and i <= 'Z':
            i = ord(i)+n
            if i> ord('Z'):
                i -= 26
        answer+=''.join(chr(i))
    return answer

# solution('z',1)
solution('a B z',4)
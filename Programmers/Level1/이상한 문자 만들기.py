def solution(s):
    answer = ''
    arr = s.split(' ')
    for i in arr:
        splited=''
        i = i.lower()
        for j in range(len(i)):
            if j%2==0:
                splited+=''.join(chr(ord(i[j])-32))
            else:
                splited+=''.join(i[j])
        answer+=''.join(splited+' ')
    return answer[:len(answer)-1]

solution("try hello world")
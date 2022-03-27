def get_time(start,end):
    return (int(end[0])-int(start[0])) * 60 + int(end[1]) - int(start[1])

def solution(m, musicinfos):
    answer = []
    for index,info in enumerate(musicinfos):
        info = info.split(',')
        playtime = get_time(info[0].split(':'),info[1].split(':')) #재생시간 구하기
        #멜로디 분할
        tmp=[]
        for i in range(len(info[3])):
            if info[3][i]=='#': # 멜로디의 음이 #인 경우 이전 저장된 계이름에 #을 붙인다.
                tmp.append(tmp.pop()+'#')
            else: tmp.append(info[3][i])
        # 재생시간으로 멜로디재조합
        n = divmod(playtime,len(tmp))
        melody = ''.join(tmp*n[0] + tmp[:n[1]])
        # 입출력 조건 검사
        for i in range(0,len(melody)-len(m)+1):
            if melody[i:i+len(m)]==m:
                if i+len(m)==len(melody):
                    answer.append((playtime,index,info[2]))
                elif melody[i+len(m)]!='#':
                    answer.append((playtime,index,info[2]))
                    break
    if not len(answer): return '(None)'
    answer.sort(key = lambda x:(x[0],-x[1])) # 재생시간 긴 음악, 먼저 입력된 음악의 우선순위로 정렬, pop하기 위해 각 우선순위별 역정렬
    return answer[-1][2]

print(solution('ABCDEFG',["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])) #HELLO
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])) #FOO
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])) #WORLD
print(solution("CCB",["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"])) #FOO
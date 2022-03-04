def getplaytime(start,end):
    endtime = end.split(':')
    starttime = start.split(':')
    playtime = (int(endtime[0])-int(starttime[0]))*60+(int(endtime[1])-int(starttime[1]))
    return playtime

def init_melody(melody):
    melody_list = []
    len_melody = len(melody)
    for i in range(len(melody)):
        if melody[i]=='#': continue
        if i==len_melody-1:
            melody_list.append(melody[i])
            continue
        if melody[i+1]=='#': 
            melody_list.append(melody[i]+melody[i+1])
        else:
            melody_list.append(melody[i])
    return melody_list

def solution(m, musicinfos):
    answer = []
    for i in musicinfos:
        music=i.split(',')
        playtime = getplaytime(music[0],music[1])
        melody = init_melody(music[3])
        m=init_melody(m)
        dm = divmod(playtime,len(melody))
        full_melody = melody*dm[0]+melody[:dm[1]]
        if len(m)>len(full_melody): continue

        flag=0
        loop_range=len(full_melody)-len(m) + 1
        for j in range(loop_range):
            isin = 1
            for k in range(len(m)):
                if m[k] != full_melody[j+k]:
                    isin=0
                    break
            if isin==1:
                flag=1
                break
        if flag==1:
            if not len(answer):
                answer.append((music[2],playtime,i))
                continue
            if playtime>answer[0][1]:
                answer.pop()
                answer.append((music[2],playtime,i))
    if not len(answer): return "(None)"
    return answer[0][0]

# print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("ABCD",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("ABC",["12:00,12:14,HELLO,C#DEFGABCA#", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("C#",["12:00,12:03,QWE,C#C","12:00,12:04,RRR,C#C#"]))

# '#'반음을 구별해서 m 과 musicinfos의 각 노래별 멜로디를 리스트로 만든다. ['C','C#',...]
# 재생시간을 구해서 노래의 전체 멜로디를 구한다.
# 전체 멜로디에 m이 포함된 경우를 찾고, answer에 삽입한다.
# 이때 answer값이 이미 존재한다면 재생시간이 더 큰 경우의 노래를 answer에 삽입한다.




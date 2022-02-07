# 베스트 앨범 수록 로직
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
from collections import defaultdict

def solution(genres, plays):
    answer = []

    g_dict = defaultdict(list) # 장르를 키로, 노래 고유번호를 리스트 값으로 가지는 장르 객체 => classic: [0,1]
    s_dict = defaultdict(int) # 노래 고유번호를 키로, 재생횟수를 정수 값으로 가지는 노래 객체 => 0:500
    data_dict =defaultdict(list) # 장르를 키로, 노래 고유번호와 전체 재생횟수로 이루어진 튜플값을 리스트로 가지는 객체 => classic:[(0,1000),(1,300)]
    for i in range(len(genres)):
        genre = genres[i]
        song = (i,plays[i])
        data_dict[genre].append(song)
        g_dict[genre].append(i)
        s_dict[i]=plays[i]

    maximum = []
    for genre in g_dict.keys():
        cnt=0
        for song in g_dict[genre]:
            cnt+=s_dict[song]
        maximum.append((genre,cnt))
    maximum.sort(key=lambda x:x[1],reverse=True)
    
    for data in maximum:
        genre = data[0]
        items = data_dict[genre] # tuple list
        items.sort(key=lambda x:(-x[1],x[0])) # 재생횟수 1순위, 횟수가 같을 시 고유번호 낮은 순서 2순위

        songs = items[:2]
        [answer.append(i) for i,v in songs]
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])) # 로직 1,2 검증
# print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 500, 2500, 2500])) # 로직 1,2,3 검증
# print(solution(["classic", "pop", "rock", "classic", "pop"],[500, 600, 3500, 500, 2500])) # 로직 3 검증
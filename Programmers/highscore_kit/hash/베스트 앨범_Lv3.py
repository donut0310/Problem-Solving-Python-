from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_dict = defaultdict(list)
    total_time_dict = defaultdict(int)

    # 초기화
    for i in range(len(genres)):
        genre_dict[genres[i]].append((i, plays[i])) # (고유번호, 재생횟수)
        total_time_dict[genres[i]] += plays[i] # 장르별 속한 노래의 전체 재생시간

    # 1. 장르별로 속한 노래가 많이 재생된 순서로 내림차순
    rank_by_totaltime = sorted(total_time_dict.items(), key = lambda x:-x[1])

    # 2. 장르 내에서 많이 재생된 노래 최대 2개
    for genre, totaltime in rank_by_totaltime:
        tmp = sorted(genre_dict[genre], key = lambda x: (-x[1], x[0]))[:2]
        [answer.append(i) for i, playtime in tmp]

    return answer

    
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])) # [4, 1, 3, 0]

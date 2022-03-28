def solution(s):
    answer,arr=[],[]
    s=s[2:-2].split('},{') #문자열 s 분리
    [arr.append(i.split(','))for i in s]
    arr.sort(key=lambda x:len(x)) # 원소길이 기준으로 정렬
    for tup in arr:
        for t in tup:
            if not int(t) in answer:
                answer.append(int(t))
    return answer
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) #[2,1,3,4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")) #[2,1,3,4]
print(solution("{{20,111},{111}}")) #[111,20]
print(solution("{{123}}")) #[123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) #[3,2,4,1]

# 풀이
# 주어진 문자열 s의 양옆 '{{' '}}'을 제거한 후 집합별 사이의 '},{' 문자열을 기준으로 분리한다.
# 각 리스트마다 숫자 사이에 포함된 콤마를 기준으로 분리한 후 arr배열에 저장한다.
# arr배열을 각 원소의 길이순으로 정렬한다.
# arr배열의 각 원소(튜플 집합)을 기준으로 answer에 배열에 삽입한다.
# 이때 이미 answer에 들어간 숫자에 대해선 무시한다.

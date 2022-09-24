from collections import defaultdict

def solution(msg):
    answer = []
    
    dict = defaultdict(int)
    for i in range(1, 27):
        dict[chr(i+64)] = i
    cnt = 27

    while True:
        for i in range(len(msg)):
            target = msg[:i+1]

            if not dict[target]:
                answer.append(dict[msg[:i]])
                dict[target] = cnt
                cnt += 1
                msg = msg[i:]
                break
            
            if i == len(msg)-1:
                answer.append(dict[target])
                return answer

print(solution("KAKAO")) # 	[11, 1, 27, 15]
print(solution("TOBEORNOTTOBEORTOBEORNOT")) # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
# k, a, ka, ao
# ka,ak,kao
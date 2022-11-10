# 방법 1
def solution(people, limit):
    answer = 0
    l, r, mid = 0, len(people) - 1, limit // 2
    cnt = 0 # 보트에 탄 사람 수

    people.sort()
    
    while l < r:
        if people[l] > mid:
            answer += r - l + 1
            return answer
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
            cnt += 2
        else:
            r -= 1
            cnt += 1
        answer += 1

    answer += len(people) - cnt
    return answer

print(solution([70, 50, 80, 50], 100)) # 3
print(solution([50, 50, 50], 100)) # 2
print(solution([50], 100)) # 1
print(solution([40, 40, 40], 40)) # 3


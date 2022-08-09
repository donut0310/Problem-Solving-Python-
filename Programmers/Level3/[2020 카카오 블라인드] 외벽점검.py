from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    tofix = len(weak)
    dist = sorted(dist, reverse=True)

    for i in range(len(weak)): # 시작점 0을 지나는 경우도 있기에 배열의 크기를 두배 늘려준다. 이때 0점을 지난 값은 각 값에 n을 더한다.
        weak.append(weak[i] + n)

    for i in range(tofix):
        arr = weak[i:] + weak[:i] # 원형 탐색을 위한 배열

        for p in permutations(dist, len(dist)): # dist 배열의 모든 순열
            fixed = set() # 수리된 지점의 위치를 저장할 집합 객체
            cnt = 0

            for index in range(len(p)):
                start = arr[cnt]
                end = start + p[index]

                for j in range(cnt, len(arr)):
                    if start <= arr[j] <= end:
                        fixed.add(arr[j] % n)
                        cnt+=1

                if len(fixed) == tofix:
                    answer = min(index + 1, answer)
                    break

    if answer > len(dist): return -1
    return answer

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4])) # 2
print(solution(12,[1, 3, 4, 9, 10], [3, 5, 7])) # 1
print(solution(200,[0, 100],[1, 1])) # 2
print(solution(200,[0, 10, 50, 80, 120, 160],[1, 10, 5, 40, 30])) # 3
print(solution(50,[1],[6])) # 1

'''
<풀이>
시작점 0을 지나는 경우에 대해, 각 수리할 지점의 위치값이 바뀌어야 한다. 따라서, 각 값에 n을 더한 값을 배열에 삽입한다.
dist 배열의 값은, 가장 큰 값부터 우선순위로 처리하는게 아니라, dist 배열의 모든 순열을 구해 조사해야한다.
1. 확장된 weak 배열을 원래 weak배열의 크기만큼 반복하며 시작점을 변경한다.
2. 시작점이 변경된 배열마다 dist 배열의 모든 순열에 대해 조사한다.
3-1. weak 배열의 시작점을 start로, dist배열의 각 원소값을 start에 더해 end값으로 범위를 지정한 후,
    arr배열을 탐색하며 범위에 해당하는 값을 fixed 집합객체에 담아준다.
3-2. 이때, 수리된 지점은 다시 조사할 필요가 없기에, cnt 값으로 weak 배열에서 조사할 위치를 조작한다.
4. fixed 집합체가 tofix와 같을 때(즉, 모든 지점이 수리가 되었을 경우) answer값을 갱신해준 뒤, 반복문을 종료한다.
5. 이후, 수리된 지점이 아예 없는 경우를 고려하여 answer 값을 반환한다.

`현재는 반복문의 다중사용으로 시간복잡도가 매우 높다. 리뷰 풀이 때 개선하는 것으로 목표!`
'''

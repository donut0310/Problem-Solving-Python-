from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    tofix = len(weak)
    perm = list(permutations(dist, len(dist)))

    for i in range(len(weak)):
        weak.append(weak[i] + n)
    
    for i in range(tofix):
        arr = weak[i:] + weak[:i] # [1, 5, 6, 10, 13, 17, 18, 22], [5, 6, 10, 13, 17, 18, 22, 1] ...
        
        for p in perm:
            fixed = set()
            cnt = 0

            for j in range(len(dist)):
                start = arr[cnt]
                end = start + p[j]

                for k in range(cnt, len(arr)):
                    if start <= arr[k] <= end:
                        fixed.add(arr[k] % n)
                        cnt += 1
                    else: break
                    
                if len(fixed) == tofix:
                    answer = min(j+1, answer)
                    break

    if answer > len(dist): return -1
    return answer

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4])) # 2
print(solution(12,	[1, 3, 4, 9, 10], [3, 5, 7])) # 1
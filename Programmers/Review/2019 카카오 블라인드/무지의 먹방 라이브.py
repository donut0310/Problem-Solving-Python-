def solution(food_times, k):
    answer = 0
    for i in range(len(food_times)):
        food_times[i] = [i, food_times[i]]

    remained = set([i for i in range(len(food_times))])
    food_times.sort(key=lambda x:x[1])

    prev = 0
    for i in range(len(food_times)):
        tmp = (food_times[i][1] - prev) * len(remained)
        prev = food_times[i][1]
        if tmp <= k:
            k -= tmp
            remained.remove(food_times[i][0])
        else:
            answer = list(remained)[k % len(remained)] + 1
            return answer
    return -1

print(solution([3, 1, 2], 5)) # 1

'''
<풀이>
음식별로 번호를 부여한 후, 남은 음식량이 적은 순으로 오름차순 정렬을 진행한다.
ex) (1,1),(2,2),(3,0) # (인덱스, 남은 음식량)
각 음식별로 1번 먹고 2번째로 먹으려면, 모든 음식을 한번씩 먹어야 하기 때문에
n(음식 개수) * x(횟수) 만큼 지날 때마다 똑같은 음식을 다시 먹을 수 있다.

이를 이용해서, 현재 시점에서의 음식을 다 먹으려면 "(현재 접시 음식의 양 - 이전 접시의 음식의 양) * 남은 음식의 수"를 도출할 수 있다.
위 식의 값(tmp)이 주어진 k보다 작다면, 시간이 남기 때문에 더 많은 음식을 먹을 수 있게 된다.
k는 k-tmp의 값으로 시간을 줄이고, 현재 접시의 음식은 남은 음식에서 제거한다.

tmp값이 k보다 크다면, 주어진 시간내에 현재 접시 이후의 모든 음식을 먹을 수 없게 되기 때문에
k값을 남은 음식의 수로 나눈 나머지는 남은 음식의 인덱스로 사용할 수 있게된다.

반복문을 통해 각 음식마다 위 과정을 반복하면 된다.
'''
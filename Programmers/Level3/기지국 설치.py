def count(cnt,size):
    x,y = divmod(cnt,size)
    if y==0: return x
    else: return x+1

def solution(n, stations, w):
    answer = 0
    start = 0
    size = 2*w+1
    for i in range(len(stations)):
        s,e = stations[i]-1-w,stations[i]-1+w
        if s<0: s=0
        if e>n-1: e=n-1
        answer += count(s-start,size)
        start=e+1
    if start<n:
        cnt=n-start
        answer+=count(cnt,size)
    return answer
   

print(solution(11, [4, 11],1)) # 3
print(solution(16, [9],2)) # 3


''' 
<풀이>
1. N개의 아파트를 배열로 만들어 각 기지국에서의 범위를 구한 후 남은 영역에 속한 아파트들을 대상으로 최소의 기지국을 건설했지만 시간초과!
2. N개의 아파트를 만들 필요 없이, 파라미터로 주어진 stations(기지국의 위치)만으로 계산이 가능하다.

stations는 오름차순으로 주어지기에, 각 기지국의 영향력이 미치는 시작범위와 끝 범위를 구한다.
start변수를 0으로 0번 아파트의 정보를 주고, 각 기지국마다 시작범위와 start변수의 차이를 더한 뒤, start변수를 기지국의 끝범위(e)로 바꿔준다.
마지막 기지국이 n번째에 있지 않다면, n-e 영역부터 n 영역까지의 값은 반복문 내에서 더해지지 않는다.
따라서, 반목문이 끝난 후, start변수의 위치를 확인하여 남은 영역까지 모두 계산해준다.
'''
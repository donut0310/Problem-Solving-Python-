def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    position = -30001

    for enter, out in routes:
        if enter <= position:
            continue
        else:
            answer += 1
            position = out

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))  # 2

'''
<풀이>
1. 차량의 진출 위치를 기준으로 오름차순 정렬
2. 첫번째 카메라의 위치를 최소범위(-30000) 보다 작은 -30001로 설정
3. 각 차량마다 진입 위치가 카메라가 설치된 위치보다 앞에 있다면, 현재 설치된 카메라를 만나기 때문에 스킵
4. 차량의 진입 위치가 카메라보다 뒤에 있다면, 현재 설치된 카메라와 만날 수 없기 때문에 설치 카메라의 수를 1 증가 시키고
    현재 차량의 진출위치에 카메라를 설치한다.
5. 위 과정을 모든 차량에 반복한다.

'''
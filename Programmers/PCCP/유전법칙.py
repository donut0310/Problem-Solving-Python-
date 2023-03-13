from collections import defaultdict

def solution(queries):
    answer = []

    for n, p in queries:
        stack = []
        flag = 0
        p -= 1
        while n > 1:
            stack.append(p % 4)
            n -= 1
            p //= 4
            
        while stack:
            tmp = stack.pop()
            if tmp == 0: 
                answer.append('RR')
                flag = 1
                break
            elif tmp == 3: 
                answer.append('rr')
                flag = 1
                break
        if not flag: answer.append('Rr')
    return answer

'''
<풀이>
n계층 p레벨을 선택하는 법
노드 번호를 0 부터 시작하도록 p 값을 -1 한다.
p를 4로 나눈 몫은 부모 계층에서의 순번을 의미하며, 나머지는 p의 형제 노드들에서의 순번을 의미한다.
1계층(루트)전 까지 부모를 타고 올라가면서 n회차에서의 나머지 값을 스택에 저장한다.
스택에서 하나씩 꺼내는데 이때 순서가 0번 째인 경우 2계층에서 부모가 RR이 되는데 RR의 유전법칙에 의하면 자식 노드는 무조건 RR이다.
반대로 3번 째인 경우 2게층에서 부모가 rr이 되는데 역시 유전법칙에 의해 자식 노드는 무조건 rr이다.
이 경우를 제외하고는 Rr이기 때문에 분기문으로 적절히 나누면 된다.
'''
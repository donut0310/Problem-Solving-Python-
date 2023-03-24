import sys
input = sys.stdin.readline

def solution():
    answer = 0
    arr = input().rstrip().split('-')
    
    arr[0] = sum(map(int, arr[0].split('+')))

    for i in range(1, len(arr)):
        arr[i] = -sum(map(int, arr[i].split('+')))
    answer = sum(arr)
    print(answer)
        
solution()

'''
<풀이>
주어진 공식을 최소 값을 만드는 경우가 되려면 '-' 연산이 있을 때 뒤에 나열되는 수들을 최대로 만들어줘서 빼줘야한다.
그러기 위해선 주어진 공식에서 '-' 마다 공식을 나눠줘야한다.

ex) 1+2+3-1+3+4-4+5+6 이 주어진다면, (1+2+3)-(1+3+4)-(4+5+6) 로 나눠줘야 '-' 연산을 할 때 마다 가장 큰 값을 빼줄 수 있다.
1. 주어진 공식을 '-' 로 분리한다. => arr[]
2. arr의 첫번째 원소가 (50)처럼 하나의 숫자일 수도 있고, (1+2+3) 과 같이 '+'으로 이루어질 수 있기 때문에 '+'로 분리한 수의 합으로 초기화한다.
3. 이후 arr의 두 번재 원소부터 '+'로 분리한 값의 총합에 '-'를 붙여 저장한다.
4. arr의 모든값을 합해주면 정답!
'''
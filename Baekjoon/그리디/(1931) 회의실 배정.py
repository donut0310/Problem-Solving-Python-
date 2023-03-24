import sys

input = sys.stdin.readline
n = int(input())
meetings = []

for i in range(n):
    start, end = map(int, input().split(' '))
    meetings.append((start, end))

def solution():
    answer = 0
    meetings.sort(key = lambda x:(x[1], x[0]))
    end = 0

    for s, e in meetings:
        if not answer or s >= end:
            answer += 1
            end = e
    print(answer)
solution()

'''
<풀이>
그리디 알고리즘 적용

최적해를 구하는 조건
1. 회의가 가장 빨리 끝나는 순서
2. 1을 만족하면서 회의 시작 시간이 빠른 순서

위 최적해를 구하는 조건을 만족하도록 meetings(회의 시간 리스트)를 정렬한다.
첫 번째 원소부터 카운트를 1 올리며 해당 원소의 회의 종료 시간으로 end(이전 회의가 끝난 시간)을 초기화 해준다.
현재 인덱스의 회의 종료 시간이 end보다 작다면 회의를 이어서 할 수 없기에 건너뛴다.
'''

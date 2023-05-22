from itertools import combinations
import sys
input = sys.stdin.readline

def solution():
    answer = []
    consonants, vowels = [], []
    c_len, v_len = 0, 0


    for i in s:
        if i in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(i)
            v_len += 1
        else: 
            consonants.append(i)
            c_len += 1

    for v_cnt in range(1, v_len + 1):
        c_cnt = l - v_cnt
        if c_cnt < 2: break

        v_c = list(map(list, combinations(vowels, v_cnt)))
        c_c = list(map(list, combinations(consonants, c_cnt)))

        for v in v_c:
            for c in c_c:
                answer.append(''.join(sorted(v + c)))

    [print(i) for i in sorted(answer)]

l, c = map(int, input().rstrip().split(' '))
s = input().rstrip().split(' ')

solution()

'''
최소 1개 모음, 최소 2개 자음, 오름차순
'''
# # hash
# from collections import defaultdict
# from itertools import combinations, permutations

# def solution(clothes):
#     answer = 0
#     clothes_dict = defaultdict(list)
#     p = []
#     c = []
    
#     for i in clothes:
#         clothes_dict[i[1]].append(i[0])
    
#     for i in clothes_dict.values():
#         p.append(i)
#     print(p)

#     return answer

# solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
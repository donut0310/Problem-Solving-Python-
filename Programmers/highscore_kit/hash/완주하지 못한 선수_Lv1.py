from collections import defaultdict

def solution(participant, completion):
    answer = ''
    
    p_dict = defaultdict(int)
    for i in participant:
        p_dict[i] += 1
    
    for i in completion:
        p_dict[i] -= 1
    
    for i in p_dict:
        if p_dict[i]: answer = i

    return answer

print(solution(["leo", "kiki", "eden"], 	["eden", "kiki"])) # "leo"
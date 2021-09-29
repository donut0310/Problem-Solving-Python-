from collections import defaultdict

def check(skill_dict,skill_tree):
    arr = [0]
    for i in list(skill_tree):
        v = skill_dict[i]
        if v:
            if len(arr)==0 and v!=1:
                return 0
            if v-arr[-1]==1:
                if arr[0]==0:
                    arr[0]=skill_dict[i]
                else:
                    arr.append(skill_dict[i])
            else:
                return 0
    return 1

def solution(skill, skill_trees):
    answer = 0
    skill_dict = defaultdict(int)
    
    for i in enumerate(skill,1):
        skill_dict[i[1]] = i[0]

    for skill_tree in skill_trees:
        answer+=check(skill_dict,skill_tree)
    
    return answer

solution("CBD",["BACDE", "CBADF", "AECB", "BDA","CD"])
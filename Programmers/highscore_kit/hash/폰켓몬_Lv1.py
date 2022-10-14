def solution(nums):
    answer = 0
    take = len(nums) // 2
    ponketmon_types = len(set(nums))
    
    if take > ponketmon_types: answer = ponketmon_types
    else: answer = take

    return answer

print(solution([3,1,2,3])) # 2
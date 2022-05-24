from collections import defaultdict
def solution(gems):
    num = len(set(gems))
    _num = len(gems) 
    start, end = 0, 0
    g_dict = defaultdict(int)
    
    arr = []
    while start < _num:
        if len(g_dict) == num:
            arr.append((start+1,end))
            g_dict[gems[start]] -= 1
            if g_dict[gems[start]] == 0: 
                del g_dict[gems[start]]
            start += 1
        elif end < _num:
            g_dict[gems[end]]+=1
            end += 1
        elif end == _num: break

    arr.sort(key=lambda x:(-(x[1]-x[0]),-x[0]))
    return [arr[-1][0],arr[-1][1]]

'''
투포인터 사용
1. 각각의 보석이 적어도 하나 이상 들어있도록 end 값을 1씩 증가 시키며 g_dict에 보석을 담는다.
2. g_dict의 길이가 보석 종류의 개수와 같다면 start값을 1씩 증가 시키며 g_dict에서 보석을 뺀다.
    이때, 현재 범위(start,end)를 arr 배열에 튜플로 저장한다.
3. 보석을 빼면서 해당 보석의 개수가 0개가 되면 g_dict에서 키를 삭제하고, 1의 과정을 반복하면서,
    각각의 보석이 적어도 하나 이상 담겨있도록 조건을 만족하도록 한다.
    이때, 각각의 보석이 적어도 하나 이상 담겨 있지 않은데 end값이 범위를 벗어나게 되면 while 루프를 종료한다. -> 더이상 조건을 만족할 수 없음
4. 튜플로 저장된 범위들을 조건에 맞게 정렬한다. => 범위가 가장 좁게 and 범위가 같다면 시작 인덱스가 작은 순
'''
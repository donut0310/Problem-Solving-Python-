def solution(sizes):
    answer = 0
    w, h = set(), set()
    
    for size in sizes:
        w.add(max(size))
        h.add(min(size))
    
    answer = max(w) * max(h)
    return answer
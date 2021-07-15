def solution(a,b):
    v_sum=0
    a_len = len(a)
    for i in range(a_len):
      v_sum += a[i]*b[i]  
    return v_sum
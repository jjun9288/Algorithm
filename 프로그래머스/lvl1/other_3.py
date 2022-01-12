def solution(absolutes, signs):
    answer = 0
    for i, j in zip(absolutes, signs):
        if j:
            answer += i
        if not j:
            answer -= i
        
    return answer
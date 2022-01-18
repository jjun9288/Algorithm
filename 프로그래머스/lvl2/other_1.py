def solution(progresses, speeds):
    answer = []
    
    while progresses:
        for i, (j, k) in enumerate(zip(progresses, speeds)):
            progresses[i] += k
        if progresses[0] >= 100:
            cnt = 0
            while progresses and progresses[0] >= 100:
                cnt += 1
                progresses.pop(0)
                speeds.pop(0)
            answer.append(cnt)
    
    return answer
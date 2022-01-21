import heapq
def solution(scoville, K):
    answer = 0
    tmp = 0
    scoville.sort()
    while(scoville[0] < K):
        if len(scoville) <= 1:
            return -1
        else:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            tmp = a + (2 * b)
            heapq.heappush(scoville, tmp)
            answer += 1
    return answer
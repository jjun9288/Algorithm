# 배열의 K번째 큰 요소

import heapq

nums = [3,2,3,1,2,4,5,5,6]
k = 4
heap = []
for n in nums:
    heapq.heappush(heap, -n)
    
for _ in range(k-1):
    heapq.heappop(heap)
    
print(-heapq.heappop(heap))


import sys
import heapq

input = sys.stdin.readline
N, K = map(int, input().split())
treasures = []
for _ in range(N):
    heapq.heappush(treasures, list(map(int, input().split())))
C = list(int(input()) for _ in range(K))
C.sort()

steal = []
result = 0
for bag in C:
    while treasures and bag >= treasures[0][0]:
        heapq.heappush(steal, -heapq.heappop(treasures)[1])
    if steal:
        result -= heapq.heappop(steal)
print(result)
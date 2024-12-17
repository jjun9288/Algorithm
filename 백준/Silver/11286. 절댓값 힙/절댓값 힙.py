# 우선순위가 필요하니 우선순위 큐, 즉 힙이 필요할 것.
import heapq
import sys

input = sys.stdin.readline
N = int(input())
pq = []
answer = []

for _ in range(N):
    num = int(input())
    if num != 0:
        heapq.heappush(pq, (abs(num), num))
    else:
        answer.append(heapq.heappop(pq)[1] if pq else 0)

for i in answer:
    print(i)
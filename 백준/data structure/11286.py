# 절댓값 힙

import heapq as hq
import sys

n = int(input())
arr = []

for _ in range(n):
    x = int(sys.stdin.readline())       #그냥 input으로 할 경우 10만 개의 input을 받으면 timeout이 나므로 빠른 입출력을 씀
    
    if x != 0:
        hq.heappush(arr, (abs(x), x))   #배열 특성상 첫번째 원소가 같으면 두번째 원소를 비교하므로 절대값에 대해 작은 값을 먼저 보냄
    else:
        print(hq.heappop(arr)[1] if arr else 0)
        
    
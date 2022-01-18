# 특정 거리의 도시 찾기

from collections import deque

n, m, k, x= map(int, input().split())
graph = []
for _ in range(n+1):
    graph.append([])

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0        

# BFS
q = deque([x])
while q:
    now = q.popleft()
    for next in graph[now]:
        #아직 방문하지 않은 도시라면
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            q.append(next)

check = False            
for i in range(len(distance)):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
        

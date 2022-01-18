# BFS
# 너비 우선 탐색. 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
# 큐 자료구조 이용
# 간선이 모두 동일한 상황에서 최단 경로 문제를 위해 사용된다.

from collections import deque

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
                
# 1하고 연결된 노드 2, 3, 8
# 2하고 연결된 노드 1,7
# 3하고 연결된 노드 1, 4, 5
# 4하고 연결된 노드 3, 5
# 5하고 연결된 노드 3, 4
# 6하고 연결된 노드 7
# 7하고 연결된 노드 2, 6, 8        
# 8하고 연결된 노드 1, 7
graph = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]]

visited = [False] * 9

BFS(graph, 1, visited)                

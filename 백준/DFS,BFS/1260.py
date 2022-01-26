# DFS와 BFS

from collections import deque

n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
    
    
def dfs(v, discovered=[]):
    discovered.append(v)
    print(v, end=' ')
    for i in range(len(graph[v])):
        if graph[v][i] == 1:
            if i not in discovered:
                dfs(i)
    

def bfs(v):
    discovered = [v]
    queue = deque([v])
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(len(graph[v])):
            if graph[v][i] == 1:
                if i not in discovered:
                    discovered.append(i)
                    queue.append(i)
           
dfs(v)
print()
bfs(v)   
# DFS

def DFS(graph, v, visited):
    
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)
            

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

DFS(graph, 1, visited)
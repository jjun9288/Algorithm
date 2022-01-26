com = int(input())
connected = int(input())

graph = [[0]*(com+1) for _ in range(com+1)]
for i in range(connected):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
def dfs(v, discovered=[]):
    discovered.append(v)
    for i in range(len(graph[v])):
        if graph[v][i] == 1 and i not in discovered:
            discovered.append(i)
            dfs(i)
    return discovered

print(dfs(1))
            
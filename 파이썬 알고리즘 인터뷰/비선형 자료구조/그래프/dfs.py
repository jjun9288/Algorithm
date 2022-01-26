graph = {
    1 : [2, 3, 4],
    2 : [5],
    3 : [5],
    4 : [],
    5 : [6, 7],
    6 : [],
    7 : [3]
}

# 1. 재귀
def dfs_recursive(v, discovered=[]):
    discovered.append(v)
    for i in graph[v]:
        if i not in discovered:
            discovered = dfs_recursive(i, discovered)
    return discovered

# 2. 스택을 이용한 반복 구조
def dfs_iterative(v):
    discovered = []
    stack = [v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

print(dfs_recursive(1))
print(dfs_iterative(1))
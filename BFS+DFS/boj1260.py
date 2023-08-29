from collections import deque

def dfs(start):
    visited[start] = True
    dfs_list.append(start+1)
    for v in graph[start]:
        if not visited[v]:
            dfs(v)
            
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        current = q.popleft()
        bfs_list.append(current+1)
        for v in graph[current]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
            
        

N, M, start = map(int, input().split())
start -= 1
graph = [[] for _ in range(N)]
for _ in range(M):
    src, dest = map(int, input().split())
    src -= 1
    dest -= 1
    graph[src].append(dest)
    graph[dest].append(src)

for g in graph:
    g.sort()

# DFS
visited = [False for _ in range(N)]
dfs_list = []
dfs(start)

# BFS
visited = [False for _ in range(N)]
bfs_list = []
bfs(start)

for p in dfs_list:
    print(p, end=" ")
print()
for p in bfs_list:
    print(p, end=" ")

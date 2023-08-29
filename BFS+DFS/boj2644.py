from collections import deque

def bfs(a, b):
    visited = [False for _ in range(n+1)]
    q = deque()
    q.append((a, 0))
    visited[a] = True
    while q:
        current, cnt = q.popleft()
        if current == b:
            print(cnt)
            return
        for p in family[current]:
            if not visited[p]:
                visited[p] = True
                q.append((p, cnt+1))
    print(-1)
    return

n = int(input())
family = [[] for _ in range(n+1)]
a, b = map(int, input().split())
nn = int(input())
for _ in range(nn):
    parent, child = map(int, input().split())
    family[parent].append(child)
    family[child].append(parent)
    
for f in family:
    f.sort()

bfs(a, b)
    
t = int(input())
stores = []
visited = []
from collections import deque

def bfs(home, goal):
    q = deque()
    q.append(home)
    while q:
        x, y = q.popleft()
        if abs(goal[0]-x) + abs(goal[1]-y) <= 1000:
            print("happy")
            return True
        for i in range(len(stores)):
            if not visited[i] and abs(stores[i][0]-x) + abs(stores[i][1]-y) <= 1000:
                visited[i] = True
                q.append(stores[i])
            


for _ in range(t):
    s = int(input())
    stores = []
    visited = [False for _ in range(s)]
    home = tuple(map(int, input().split()))
    for _ in range(s):
        x, y = map(int, input().split())
        stores.append((x, y))
    goal = tuple(map(int, input().split()))
    if bfs(home, goal):
        continue
    print("sad")


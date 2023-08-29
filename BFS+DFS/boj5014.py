from collections import deque


def bfs():
    global F, S, G, U, D
    q = deque()
    q.append((S,0))
    visited[S] = True
    while q:
        current, count = q.popleft()
        if current == G :
            print(count)
            exit()
        up = current + U
        down = current - D
        if 0<=up<=F and not visited[up]:
            visited[up] = True
            q.append((up, count + 1))
        if 0<=down<=F and not visited[down]:
            visited[down] = True
            q.append((down, count + 1))
            
    


F, S, G, U, D = map(int, input().split())
visited = [False for _ in range(F+1)]
visited[0] = True
bfs()
print("use the stairs")
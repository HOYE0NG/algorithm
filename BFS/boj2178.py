from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0 ,0]

def bfs(start):
    x, y = start
    q = deque()
    cnt = 1
    q.append((x, y, cnt))
    while q:
        x, y, cnt = q.popleft()
        print(x, y)
        if visited[x][y]:
            continue
        visited[x][y] = True
        if x == N-1 and y == M-1:
            print(cnt)
            return
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0<=ax<N and 0<=ay<M:
                if board[ax][ay] == 1 and not visited[ax][ay]:
                    q.append((ax, ay, cnt + 1))         

N, M = map(int, input().split())
board = []
visited = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    s = list(map(int, list(input())))
    board.append(s)
        
bfs((0,0))
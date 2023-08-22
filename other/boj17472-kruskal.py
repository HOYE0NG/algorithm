from collections import deque

def bfs(pos, i_num):
    x, y = pos
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    islands[i_num].append((x, y))
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            ax = xx + dx[i]
            ay = yy + dy[i]
            if 0<=ax<N and 0<=ay<M:
                if not visited[ax][ay] and board[ax][ay] == 1:
                    visited[ax][ay] = True
                    islands[i_num].append((ax, ay))
                    q.append((ax, ay))

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

        
    
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * M for _ in range(N)]
islands = []
i_num = -1
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not visited[i][j]:
            islands.append([])
            i_num += 1
            bfs((i,j), i_num)

for island in islands:
    for pos in island:
        print(pos)
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(pos):
    x, y = pos
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 1
    while q :
        x, y = q.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0<=ax<N and 0<=ay<N:
                if not visited[ax][ay] and board[ax][ay] == 1:
                    visited[ax][ay] = True
                    q.append((ax, ay))
                    cnt += 1
    return cnt
        

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, list(input()))))

visited = [[False for _ in range(N)] for _ in range(N)]
result = []
cnt = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            result.append(bfs((i, j)))
            cnt += 1
            
print(cnt)
result.sort()
for r in result:
    print(r)

            
            
            
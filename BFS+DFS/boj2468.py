from collections import deque

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

water_height = 0
result = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0 ,0]

def bfs(pos, visited):
    global water_height
    x, y = pos
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0<=ax<N and 0<=ay<N:
                if board[ax][ay] > water_height and not visited[ax][ay]:
                    visited[ax][ay] = True
                    q.append((ax, ay))


q = deque()
while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > water_height and not visited[i][j]:
                bfs((i, j), visited)
                count += 1
    if count > result:
        result = count
    if count == 0:
        break 
    water_height += 1
        
    
print(result)
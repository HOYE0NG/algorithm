from copy import deepcopy
from collections import deque

N, M = map(int, input().split())
board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
years = 0

for _ in range(N):
    board.append(list(map(int, input().split())))

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q :
        x, y = q.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if not visited[ax][ay] and board[ax][ay] > 0:
                visited[ax][ay] = True
                q.append((ax, ay))

count = 0

while True:
    visited = [[False for _ in range(M)] for _ in range(N)]
    years += 1
    flag = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and not visited[i][j]:
                flag = 1
                visited[i][j] = True
                for k in range(4):
                    ax = i + dx[k]
                    ay = j + dy[k]
                    if board[ax][ay] <= 0 and not visited[ax][ay] :
                        board[i][j] -= 1
    
    if flag == 0:
        print(0)
        exit()
        
    flag = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and not visited[i][j]:
                if flag == 1:
                    print(years)
                    exit()
                flag = 1
                bfs(i, j, visited)


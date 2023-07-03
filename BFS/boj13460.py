import sys
from collections import deque

def move(x, y, dx, dy):
    cnt = 0
    while board[x][y] != "O" and board[x+dx][y+dy] != "#":
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs(red_x, red_y, blue_x, blue_y):
    q = deque()
    q.append([red_x, red_y, blue_x, blue_y, 0])
    visited[red_x][red_y][blue_x][blue_y] = True
    cnt = 0
    
    while q:
        current = q.popleft()
        d = current[4]
        if d >= 10:
            print(-1)
            return
        
        for i in range(4):
            red_ax, red_ay, red_cnt = move(current[0], current[1], dx[i], dy[i])
            blue_ax, blue_ay, blue_cnt = move(current[2], current[3], dx[i], dy[i])
            if red_cnt != 0 or blue_cnt != 0:
                if board[blue_ax][blue_ay] == "O":
                    continue
                if board[red_ax][red_ay] == "O":
                    print(d+1)
                    return
                if red_ax == blue_ax and red_ay == blue_ay:
                    if red_cnt > blue_cnt:
                        red_ax -= dx[i]
                        red_ay -= dy[i]
                    else:
                        blue_ax -= dx[i]
                        blue_ay -= dy[i]
                
                if not visited[red_ax][red_ay][blue_ax][blue_ay] :
                    visited[red_ax][red_ay][blue_ax][blue_ay] = True
                    q.append([red_ax, red_ay, blue_ax, blue_ay, d+1])
    
    print(-1)
    return
        
N, M = map(int , input().split())
board = [list(input().strip()) for _ in range(N)]
visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

blue_x = 0
blue_y = 0
red_x = 0
red_y = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == "B":
            blue_x = i
            blue_y = j
        if board[i][j] == "R":
            red_x = i
            red_y = j
            
bfs(red_x, red_y, blue_x, blue_y)


    
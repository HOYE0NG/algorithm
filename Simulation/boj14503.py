from collections import deque

N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(pos):
    x, y = pos
    global d
    q = deque()
    q.append((x,y))
    board[x][y] = 2
    count = 1
    while q:
        x, y = q.popleft()
        flag = 0
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0<=ax<N and 0<=ay<M:
                if board[ax][ay] == 0:
                    flag = 1
                    break
        if flag == 0:
            ax = x - dx[d]
            ay = y - dy[d]
            if 0<=ax<N and 0<=ay<M:
                q.append((ax, ay))
            else:
                print(count)
                return
        else:
            for _ in range(4):
                d -= 1
                if d<0:
                    d = 3
                ax = x + dx[d]
                ay = y + dy[d]
                if 0<=ax<N and 0<=ay<M:
                    if board[ax][ay] == 0:
                        count += 1
                        board[ax][ay] = 2
                        q.append((ax, ay))
                        break
    
            
                    
        

bfs((x, y))
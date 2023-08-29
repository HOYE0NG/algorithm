from collections import deque

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    global goal
    global last
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            az = z + dz[i]
            ax = x + dx[i]
            ay = y + dy[i]
            if 0<=az<H and 0<=ax<M and 0<=ay<N:
                if board[az][ax][ay] == 0:
                    goal -= 1
                    board[az][ax][ay] = board[z][x][y] + 1
                    last = board[az][ax][ay]
                    q.append((az, ax, ay))
                    
N, M, H = map(int, input().split())

board = []
goal = 0
last = 0
for _ in range(H):
    b = []
    for _ in range(M):
        b.append(list(map(int, input().split())))
    board.append(b)
    
q = deque()

for i in range(H):
    for j in range(M):
        for k in range(N):
            if board[i][j][k] == 1:
                q.append((i, j, k))
            if board[i][j][k] == 0:
                goal += 1

if goal == 0:
    print(0)

bfs()

if goal != 0:
    print(-1)
else:
    print(last-1)
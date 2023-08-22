from collections import deque

def snake_move():
    global cnt
    cnt += 1
    head = []
    head.append(snake[0][0])
    head.append(snake[0][1])
    head[0] += direction[0]
    head[1] += direction[1]
    if 0<=head[0]<N and 0<=head[1]<N:
        for s in snake:
            if head[0] == s[0] and head[1] == s[1]:
                return False
        if board[head[0]][head[1]] == 1:
            snake.appendleft([head[0], head[1]])
        else:
            snake.appendleft([head[0], head[1]])
            snake.pop()
        return True
    else:
        return False
    
# board
N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]

# apple
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    board[x][y] = 1

# rotation
R = int(input())
rotation = []
for _ in range(R):
    s, r = input().split()
    sec = int(s)
    rotation.append((sec, r))

# snake
snake = deque()
snake.append([0,0])
cnt = 0 

# direction 우 하 좌 상 L: +1 D: -1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0
direction = (dx[d], dy[d])

while True:
    
    if rotation and cnt == rotation[0][0]:
        print(rotation)
        if rotation[0][1] == 'D':
            d = (d+1)%4
            direction = (dx[d], dy[d])
        else:
            d -= 1
            if d<0:
                d = 3
            direction = (dx[d], dy[d])
        del rotation[0]
    if not snake_move():
        break

print(cnt)



    
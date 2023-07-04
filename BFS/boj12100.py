import sys
from collections import deque
from copy import deepcopy

def move(board, dx, dy):
    max = 0
    can_combined = [[True for _ in range(N)] for _ in range(N)]
    start_idx = 0
    end_idx = 0 
    step = 0
    if (dx == -1 and dy == 0) or (dx == 0 and dy == -1):
        start_idx, end_idx, step = 0, N, 1
    else:
        start_idx, end_idx, step = N-1, -1, -1
    
    for i in range(start_idx, end_idx, step):
        for j in range(start_idx, end_idx, step):
            if board[i][j] == 0:
                continue
            ax, ay = i, j
            while (ax+dx>=0 and ay+dy>=0 and ax+dx<N and ay+dy<N) and board[ax+dx][ay+dy] == 0:
                ax += dx
                ay += dy
                board[ax][ay] = board[ax-dx][ay-dy]
                board[ax-dx][ay-dy] = 0
            if (ax+dx>=0 and ay+dy>=0 and ax+dx<N and ay+dy<N) and (board[ax][ay] == board[ax+dx][ay+dy]) and can_combined[ax+dx][ay+dy]:
                board[ax+dx][ay+dy] *= 2
                board[ax][ay] = 0
                if max < board[ax+dx][ay+dy]:
                    max = board[ax+dx][ay+dy]
                can_combined[ax+dx][ay+dy] = False
             
    return board, max
            

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

max_value = 0
for i in range(N):
    for j in range(N):
        if max_value < board[i][j]:
            max_value = board[i][j]

# bfs         
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
q = deque()
q.append([board, 0])

while q:
    current_board, count = q.popleft()
    if count == 5:
        print(max_value)
        break
    for i in range(4):
        next_board, max = move(deepcopy(current_board), dx[i], dy[i])
        if max > max_value:
            max_value = max
        print(next_board)
        q.append([next_board, count + 1])
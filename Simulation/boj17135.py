from copy import deepcopy
from collections import deque

N, M, D = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
b = []
case = []
result = 0
enemy_num = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            enemy_num +=1
            
def enemy_attack():
    for i in range(N-1, 0, -1):
        for j in range(M):
            b[i][j] = b[i-1][j]
    for j in range(M):
        b[0][j] = 0

def shoot(arrow):
    dx = [0, -1, 0]
    dy = [-1, 0, 1]
    q = deque()
    q.append([N-1, arrow, 1])
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[N-1][arrow] = True
    while q:
        x, y, cnt = q.popleft()
        if cnt > D:
            return 0, 0, False
        
        if b[x][y] == 1:
            return x, y, True
        else:
            for i in range(3):
                ax = x + dx[i]
                ay = y + dy[i]
                if ax >= 0 and ay >= 0 and ax < N and ay < M :
                    if not visited[ax][ay] :
                        q.append([ax,ay,cnt+1])
                        visited[ax][ay] = True
    return 0, 0, False
            
            
    

for i in range(0, M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            case.append([i,j,k])
            
for c in case:
    now_result = 0
    b = deepcopy(board)
    for _ in range(N): # line
        killed_enemy = set()
        for arrow in c:
            x, y, is_killed = shoot(arrow)
            if is_killed:
                killed_enemy.add((x, y))
        for enemy in killed_enemy:
            b[enemy[0]][enemy[1]] = 0
            now_result += 1
            if enemy_num == now_result:
                print(now_result)
                exit()
        enemy_attack()
    if now_result > result:
        result = now_result
        
print(result)

        
    
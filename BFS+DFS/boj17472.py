from collections import deque
from itertools import combinations

def get_islands_pos(start):
    global islands
    global islands_num
    
    q = deque()
    q.append(start)
    islands[islands_num].append(start)
    visited[start[0]][start[1]] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0<=ax<N and 0<=ay<M:
                if board[ax][ay] == 1:
                    if not visited[ax][ay]:
                        visited[ax][ay] = True
                        islands[islands_num].append((ax, ay))
                        q.append((ax, ay))
        
def bfs(links):
    visited = [False]*islands_num
    start = links[0][0]
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        src = q.popleft()
        for link in links:
            if src == link[0]:
                if not visited[link[1]]:
                    visited[link[1]] = True
                    q.append(link[1])
            if src == link[1]:
                if not visited[link[0]]:
                    visited[link[0]] = True
                    q.append(link[0])
    for v in visited:
        if not v:
            return False
    return True

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
islands = []
islands_num = -1
bridges = []
my_result = 100

visited = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not visited[i][j]:
            islands.append([])
            islands_num += 1
            get_islands_pos((i, j))

            
for island_idx, island in enumerate(islands):
    for pos in island:
        x, y = pos
        for i in range(4):
            length = 0 
            i_num = -1
            ax = x + dx[i]
            ay = y + dy[i]
            # 다른 섬으로 이동하기
            while 0<=ax<N and 0<=ay<M and board[ax][ay] == 0:
                length += 1
                ax += dx[i]
                ay += dy[i]    
            # 이동할 수 없는 경우
            if length <= 1 or (ax>=N or ax<0 or ay>=M or ay<0):
                continue
            # 도착한 섬 번호
            for _i in range(island_idx+1, len(islands)):
                _island = islands[_i]
                if (ax, ay) in _island:
                    i_num = _i
            # 이전에 이미 넣은 다리
            if i_num == -1:
                continue
            bridge = (island_idx, i_num, length, (x+dx[i], y+dy[i]), (ax-dx[i], ay-dy[i]))
            # 이미 넣은 다리
            if bridge in bridges:
                continue
            bridges.append(bridge)

bridges_num = len(bridges)
islands_num = len(islands)

cases = list(combinations(bridges, islands_num-1))
for case in cases:
    result = 0
    links = []   

    for bridge in case:
        links.append((bridge[0], bridge[1]))
        result += bridge[2]


    if bfs(links):
        my_result = min(result, my_result)
    
print(-1 if my_result == 100 else my_result)

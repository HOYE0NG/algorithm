import sys
sys.setrecursionlimit(10**5)

def dfs(fx, fy, rx, ry):
    global ans
    
    if rx == N-1 and ry == N-1:
        ans += 1
        return
    # 가로
    if fx == rx:
        if ry+1 < N and board[rx][ry + 1] != 1:
            dfs(fx, fy+1, rx, ry+1)
        if ry+1 < N and rx+1 < N and board[rx][ry + 1] != 1 and board[rx+1][ry+1] != 1 and board[rx+1][ry] != 1:
            dfs(fx, fy+1, rx+1, ry+1)
    
    # 세로
    if fy == ry:
        if rx+1 < N and board[rx+1][ry] != 1:
            dfs(fx+1, fy, rx+1, ry)
        if rx+1 < N and ry+1 < N and board[rx][ry + 1] != 1 and board[rx+1][ry+1] != 1 and board[rx+1][ry] != 1:
            dfs(fx+1, fy, rx+1, ry+1)
        
    # 대각선
    if fx != rx and fy != ry :
        if ry+1 < N and board[rx][ry+1] != 1:
            dfs(fx+1, fy+1, rx, ry+1)        
        if rx+1 < N and board[rx+1][ry] != 1:
            dfs(fx+1, fy+1, rx+1, ry)
        if rx+1 < N and ry+1 < N and board[rx][ry + 1] != 1 and board[rx+1][ry+1] != 1 and board[rx+1][ry] != 1:
            dfs(fx+1, fy+1, rx+1, ry+1)
   
    
    
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

if board[N-1][N-1] == 1:
    print(0)
    sys.exit()
    
ans = 0
dfs(0,0,0,1)

print(ans)
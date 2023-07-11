import sys
sys.setrecursionlimit(10**6)

def check_size(x, y, size):
    for i in range(x, x+size+1):
        for j in range(y, y+size+1):
            if board[i][j] == 0:
                return False
    return True

def dfs(x, y, cnt):
    global result
    # 종료 조건
    if x > 9:
        result = min(cnt, result)
        return
    # 인덱스 넘어갈 때
    if y > 9:
        dfs(x+1, 0, cnt)
        return
    if board[x][y] == 1:
        for i in range(5):
            if x+i > 9 or y+i > 9: continue # 인덱스 넘어갈 때
            if papers[i] < 1 : continue # 붙일 색종이가 없을 때
            if not check_size(x, y, i): break # 색종이 붙일 수 없을 때
            # 색종이를 붙임
            for ii in range(x, x+i+1):
                for jj in range(y, y+i+1):
                    board[ii][jj] = 0        
            papers[i] -= 1
            # 다음 노드로 이동
            dfs(x, y+i+1, cnt+1)
            # 원상복귀
            papers[i] += 1
            for ii in range(x, x+i+1):
                for jj in range(y, y+i+1):
                    board[ii][jj] = 1
    else: 
        dfs(x, y+1, cnt)
        
    return # 여기 도달하면 pruning 된 것

board = [list(map(int, input().split())) for _ in range(10)]
result = 26
papers = [5, 5, 5, 5, 5]
dfs(0, 0, 0)
print(-1 if result == 26 else result)
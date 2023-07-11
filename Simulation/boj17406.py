from itertools import permutations
from copy import deepcopy



def print_board(b):
    print("--배열 시작--")
    for i in range(len(b)):
        for j in range(len(b[0])):
            print(b[i][j], end=" ")
        print()
    print("--배열 끝--")

dx = [1,0,-1,0]
dy = [0,1,0,-1]
def rotate(topleft, bottomright):
    while topleft != bottomright:
        tl_x, tl_y = topleft
        br_x, br_y = bottomright
        x, y = topleft
        distance = br_x - tl_x
        save_value = case_board[x][y]
        for i in range(4):
            for _ in range(distance):
                ax = x + dx[i]
                ay = y + dy[i]
                case_board[x][y] = case_board[ax][ay]
                x = ax
                y = ay
        case_board[x][y+1] = save_value
        tl_x += 1
        tl_y += 1
        br_x -= 1
        br_y -= 1
        topleft = (tl_x, tl_y)
        bottomright = (br_x, br_y)

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
rotations = [list(map(int, input().split())) for _ in range(K)]
cases = list(permutations(rotations, K))

result = 10000

for case in cases: # 각각의 로테이션 순열 경우의 수
    case_board = deepcopy(board)
    for rotation in case: # 로테이션 순서대로 실행
        r, c, s = rotation
        topleft = (r-s-1, c-s-1)
        bottomright = (r+s-1, c+s-1)
        rotate(topleft, bottomright)
    # 행렬의 값 계산
    value = 10000
    for i in range(N):
        v = 0
        for j in range(M):
            v += case_board[i][j]
        if v < value:
            value = v
    # 최소값?
    if value < result:
        result = value

print(result)


            
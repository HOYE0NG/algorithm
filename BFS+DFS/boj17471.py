from itertools import combinations
import sys
sys.setrecursionlimit(10**5)
def dfs(n):
    visited[n] = True
    for city in adj_list[n]:
        if not visited[city-1]:
            dfs(city-1)

def dfs_count(n):
    global pop
    pop += population[n]
    
    visited[n] = True
    for city in adj_list[n]:
        if not visited[city-1]:
            dfs_count(city-1)

def bfs(local1):

    from collections import deque
    for i in range(len(visited)):
        visited[i] = False
    q = deque()
    q.append(local1[0])
    visited[local1[0]] = True
    while q:

        now = q.popleft()
        for city in adj_list[now]:
            city = city-1
            if city in local1:
                if not visited[city]:
                    visited[city] = True
                    q.append(city)
    for city in local1:
        if not visited[city]:
            for i in range(len(visited)):
                visited[i] = False
            return False
    for i in range(len(visited)):
        visited[i] = False
    return True

def dfs_(start, local1, local2, lv):
    global my_result
    if lv == N:
        if len(local2) == 0:
            return
        if not bfs(local1):
            return
        if not bfs(local2):
            return
        result = 0
        for city in local1:
            result += population[city]
        for city in local2:
            result -= population[city]
        if abs(result) < my_result:
            my_result = abs(result)
        return
    
    # case1
    local1.append(start+1)
    dfs_(start+1, local1, local2, lv+1)
    del local1[len(local1)-1]
    
    # case2
    local2.append(start+1)
    dfs_(start+1, local1, local2, lv+1)
    del local2[len(local2)-1]


N = int(input())
population = list(map(int, input().split()))
adj_list = [list(map(int, input().split())) for _ in range(N)]
my_result = 1001
for city in adj_list: del city[0]

num = 0
pop = 0
visited = [False for _ in range(N)]
for i in range(N):
    if not visited[i]:
        dfs(i)
        num += 1

visited = [False for _ in range(N)]
if num == 2:
    pop1 = 0
    pop2 = 0
    for i in range(N):
        if not visited[i]:

            dfs_count(i)

            if i == 0:
                pop1 = pop
                pop = 0
            else:
                pop2 = pop
                pop = 0
    result = abs(pop1-pop2)
    print(result)
    
elif num == 1:
    local1 = []
    local2 = []
    local1.append(0)
    dfs_(0, local1, local2, 1)
    print(my_result)
else:
    print(-1)
    exit()

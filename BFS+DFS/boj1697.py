from collections import deque

N, K = map(int, input().split())
cnt = 0

if N >= K:
    while N != K:
        cnt += 1
        N -= 1
    print(cnt)
    exit()

visited = [False for _ in range(100001)] 
visited[0] = True

def bfs(now):
    global K
    q = deque()
    q.append((now, 0))
    visited[now] = True
    while q:
        current, count = q.popleft()
        
        if current == K:
            print(count)
            return
        
        if 0 < current and not visited[current-1]:
            visited[current-1] = True
            q.append((current-1, count+1))
        if current < 100000 and not visited[current+1]:
            visited[current+1] = True
            q.append((current+1, count+1))
        if current*2 < 100000 and not visited[current*2]:
            visited[current*2] = True
            q.append((current*2, count+1))
            
    

bfs(N)
from collections import deque

ans = 0
minLen = 100000
visited = [100000 for i in range(200000)]
N, K = map(int, input().split())

q = deque([(N, 0)])

while q:
    n, l = q.popleft()
    
    if minLen < l:
        break
    
    if n==K:
        minLen = l
        ans += 1
        continue
    
    if n-1 >= 0 and visited[n-1]>=l:
        visited[n-1] = l
        q.append((n-1, l+1))
    if n+1 < 200000 and visited[n+1]>=l:
        visited[n+1] = l
        q.append((n+1, l+1))
    if n*2 < 200000 and visited[n*2]>=l:
        visited[n*2] = l
        q.append((n*2, l+1))

print(minLen)
print(ans)
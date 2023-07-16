from collections import deque

A, B = map(int, input().split())
q = deque([(A, 1)])
ans = -1

while q:
    n, d = q.popleft()
    
    if n==B:
        ans = d
        break
    
    if n>B:
        continue
    
    q.append((n*2, d+1))
    q.append((n*10 + 1, d+1))

print(ans)
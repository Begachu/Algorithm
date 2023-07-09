from collections import deque
import sys
input = sys.stdin.readline

(N, M) = list(map(int, input().split()))
_map = [input() for n in range(N)]

visited = [[False for m in range(M)] for n in range(N)]
answer = 0
q = deque()

for n in range(N):
    for m in range(M):
        if _map[n][m] == "I":
            q.append((n, m))
            visited[n][m] = True
            break
    if q:
        break

while q:
    (n, m) = q.popleft()
    if _map[n][m] == "P":
        answer += 1
    
    if n-1 >= 0 and _map[n-1][m]!="X" and not visited[n-1][m]:
        visited[n-1][m] = True
        q.append((n-1, m))
    if n+1 < N and _map[n+1][m]!="X" and not visited[n+1][m]:
        visited[n+1][m] = True
        q.append((n+1, m))
    if m-1 >= 0 and _map[n][m-1]!="X" and not visited[n][m-1]:
        visited[n][m-1] = True
        q.append((n, m-1))
    if m+1 < M and _map[n][m+1]!="X" and not visited[n][m+1]:
        visited[n][m+1] = True
        q.append((n, m+1))

print(answer if answer > 0 else "TT")
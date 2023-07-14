from collections import deque
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
edge = [[-1 for x in range(N+1)] for y in range(N+1)]

for e in range(E):
  a, b, c = map(int, input().split())
  if edge[a][b] == -1:
    edge[a][b] = c
    edge[b][a] = c
  else:
    edge[a][b] = min(edge[a][b], c)
    edge[b][a] = min(edge[b][a], c)

v1, v2 = map(int, input().split())
cnt = [[-1 for n in range(N+1)] for i in range(3)]
cnt[0][1] = 0
cnt[1][v1] = 0
cnt[2][N] = 0

q = deque([(1, 0), (v1, 1), (N, 2)])

while q:
  n, idx = q.popleft()

  for i in range(1, N+1):
    if edge[n][i] == -1:
      continue

    if cnt[idx][i] == -1 or edge[n][i] + cnt[idx][n] < cnt[idx][i]:
      cnt[idx][i] = edge[n][i] + cnt[idx][n]
      q.append((i, idx))

if cnt[0][N] == -1 or cnt[0][v1] == -1 or cnt[0][v2] == -1:
  print(-1)
else:
  print(min(cnt[0][v1] + cnt[2][v2], cnt[0][v2] + cnt[2][v1]) + cnt[1][v2])
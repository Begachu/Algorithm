from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
T = list(map(int, input().split()))
E = [[sys.maxsize for j in range(N)] for i in range(N)]

for r in range(R):
  a, b, l = map(int, input().split())

  E[a-1][b-1] = min(E[a-1][b-1], l)
  E[b-1][a-1] = min(E[b-1][a-1], l)

answer = 0

for i in range(N):
  temp = 0
  q = deque([i])
  cnt = [sys.maxsize for n in range(N)]
  cnt[i] = 0

  while q:
    n = q.popleft()

    for j in range(N):
      c = E[n][j] + cnt[n]
      if c > M or c > cnt[j]:
          continue
      cnt[j] = c
      q.append(j)

  for j in range(N):
    if cnt[j] <= M:
      temp += T[j]
  
  answer = max(answer, temp)

print(answer)
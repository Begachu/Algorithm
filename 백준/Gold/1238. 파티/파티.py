import heapq
import sys
input = sys.stdin.readline

(N, M, X) = map(int, input().split())

edge = [[sys.maxsize for j in range(N+1)] for i in range(N+1)]

for m in range(M):
    (A, B, T) = map(int, input().split())
    edge[A][B] = T

come = [sys.maxsize for n in range(N+1)]
go = [sys.maxsize for n in range(N+1)]

come[X] = 0
go[X] = 0

heap_c = [(0, X)]
heap_g = [(0, X)]

while heap_c:
    (t, n) = heapq.heappop(heap_c)
    for i in range(1, N+1):
        if edge[n][i] != sys.maxsize and edge[n][i] + t < come[i]:
            come[i] = edge[n][i] + t
            heapq.heappush(heap_c, (come[i], i))

while heap_g:
    (t, n) = heapq.heappop(heap_g)
    for i in range(1, N+1):
        if edge[i][n] != sys.maxsize and edge[i][n] + t < go[i]:
            go[i] = edge[i][n] + t
            heapq.heappush(heap_g, (go[i], i))

print(max([come[i] + go[i] for i in range(1, N+1)]))
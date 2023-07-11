import heapq
import sys
input = sys.stdin.readline

N = int(input())  # 도시 개수(node)
M = int(input())  # 버스 개수(edge)

edge = [[sys.maxsize for j in range(N)] for i in range(N)]

for m in range(M):
    u, v, t = map(int, input().split()) # 출발지, 도착지, 비용
    if edge[u-1][v-1] > t:
      edge[u-1][v-1] = t

# 출발지, 도착지
A, B = map(int, input().split())

cnt = [sys.maxsize for n in range(N)] # 최소 비용
route = [[] for n in range(N)]        # 최소 비용 경로

cnt[A-1] = 0
route[A-1] = [str(A)]
hq = [(0, A-1)]

while hq:
    t, n = heapq.heappop(hq)
    
    for i in range(N):
        if edge[n][i] == sys.maxsize:
            continue
        if edge[n][i] + t < cnt[i]:
            cnt[i] = edge[n][i] + t
            route[i] = route[n] + [str(i+1)]
            heapq.heappush(hq, (cnt[i], i))

print(cnt[B-1])
print(len(route[B-1]))
print(' '.join(route[B-1]))
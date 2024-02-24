# 농장 관리 : 골드 5
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]

answer = 0
visited = [[False for m in range(M)] for n in range(N)]
D = [(0, -1), (0, 1), (-1, -1), (1, -1), (-1, 0), (1, 0), (1, 1), (-1, 1)]

for n in range(N):
    for m in range(M):

        if visited[n][m]:
            continue

        queue = deque([(n, m)])
        flag = True

        while queue:
            y, x = queue.pop()
            visited[y][x] = True
            
            for dy, dx in D:
                if y+dy>=0 and y+dy<N and x+dx>=0 and x+dx<M:
                    if A[y][x] == A[y+dy][x+dx] and not visited[y+dy][x+dx]:
                        queue.append((y+dy, x+dx))
                    elif A[y][x] < A[y+dy][x+dx]:
                        flag = False

        if flag:
            answer += 1

print(answer)
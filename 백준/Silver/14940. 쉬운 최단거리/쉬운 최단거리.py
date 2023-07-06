from collections import deque
import sys
input = sys.stdin.readline

(N, M) = list(map(int, input().split()))
_map = [list(map(int, input().split())) for n in range(N)]
answer = [["0" for m in range(M)] for n in range(N)]

# 시작지점 찾기
def findStart():
    for n in range(N):
        for m in range(M):
            if _map[n][m] == 2:
                return [n, m]

# BFS로 탐색 시작
def bfs():
    global start, N, M, _map, answer
    visited = [[False for m in range(M)] for n in range(N)]
    visited[start[0]][start[1]] = True
    q = deque([(start[0], start[1], 0)])

    while q:
        (n, m, l) = q.popleft()
        answer[n][m] = str(l)

        if m-1 >= 0 and _map[n][m-1] == 1 and not visited[n][m-1]:
            visited[n][m-1] = True
            q.append((n, m-1, l+1))
            
        if m+1 < M and _map[n][m+1] == 1 and not visited[n][m+1]:
            visited[n][m+1] = True
            q.append((n, m+1, l+1))
            
        if n-1 >= 0 and _map[n-1][m] == 1 and not visited[n-1][m]:
            visited[n-1][m] = True
            q.append((n-1, m, l+1))
            
        if n+1 < N and _map[n+1][m] == 1 and not visited[n+1][m]:
            visited[n+1][m] = True
            q.append((n+1, m, l+1))
        

    # 못가는 곳에 대한 표시
    for n in range(N):
        for m in range(M):
            if _map[n][m] == 1 and not visited[n][m]:
                answer[n][m] = "-1"


def printAnswer():
    global answer

    for line in answer:
        print(' '.join(line))

start = findStart()
bfs()
printAnswer()
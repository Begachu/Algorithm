from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [input() for i in range(N)]
visited = [[0]*M for _ in range(N)] 
answer = 0

for y in range(N):
    for x in range(M):
        if visited[y][x]:
            continue
        answer += 1
        _y, _x = (y, x)
        stack = deque([(y, x)])

        while visited[_y][_x]==0:
            visited[_y][_x] = answer
            if A[_y][_x] == "U" and _y-1>=0:
                _y -= 1
            if A[_y][_x] == "D" and _y+1<N:
                _y += 1
            if A[_y][_x] == "L" and _x-1>=0:
                _x -= 1
            if A[_y][_x] == "R" and _x+1<M:
                _x += 1
            stack.append((_y, _x))
        
        if visited[_y][_x] != answer:
            while stack:
                __y, __x = stack.pop()
                visited[__y][__x] = visited[_y][_x]
            answer -= 1

print(answer)
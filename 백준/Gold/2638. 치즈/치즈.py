from collections import deque
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for n in range(N)]
round = -1

D = [(-1, 0), (0, -1), (0, 1), (1, 0)]

while True:
    round += 1
    _A = copy.deepcopy(A)
    
    visited = [[False for m in range(M)] for n in range(N)]
    visited[0][0] = True
    q = deque([(0, 0)])
    c_q = deque()
    
    while q:
        n, m = q.popleft()
        for dn, dm in D:
            _n = n + dn
            _m = m + dm

            if _n < 0 or _n >= N or _m < 0 or _m >= M or visited[_n][_m]:
                continue
            
            visited[_n][_m] = True

            if _A[_n][_m] == 0:
                q.append((_n, _m))

            else:
                c_q.append((_n, _m))
    if c_q:
        while c_q:
            n, m = c_q.popleft()
            air = 0

            for dn, dm in D:
                _n = n + dn
                _m = m + dm

                if _n < 0 or _n >= N or _m < 0 or _m >= M:
                    continue

                if _A[_n][_m] == 0 and visited[_n][_m]:
                    air += 1
                    
            if air >= 2:
                A[n][m] = 0

    else:
        break
print(round)
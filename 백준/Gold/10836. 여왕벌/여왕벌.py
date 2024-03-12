import sys
input = sys.stdin.readline

M, N = map(int, input().split())
A = [[1]*M for _ in range(M)]

for _ in range(N):
    _A = [[0]*M for _ in range(M)]
    grow = list(map(int, input().split()))

    for i in range(2*M-1):
        y = max(M-i-1, 0)
        x = max(i-M+1, 0)

        for j in range(3):
            if grow[j]==0:
                continue
            grow[j] -= 1
            _A[y][x] = j
            A[y][x] += j
            break
    
    for y in range(1, M):
        for x in range(1, M):
            _A[y][x] = max(_A[y][x-1],_A[y-1][x-1],_A[y-1][x])
            A[y][x] += _A[y][x]

for y in range(M):
    print(" ".join(map(str, A[y])))
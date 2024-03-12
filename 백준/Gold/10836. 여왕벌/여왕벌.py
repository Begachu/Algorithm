import sys
input = sys.stdin.readline

M, N = map(int, input().split())
A = [[1]*M for _ in range(M)]
S = [0 for i in range(M)]

for _ in range(N):
    grow = list(map(int, input().split()))

    x0 = max(0, grow[0]-M)
    x1 = max(0, grow[0]+grow[1]-M)

    for i in range(2*M-1):
        y = max(M-i-1, 0)
        x = max(i-M+1, 0)

        for j in range(3):
            if grow[j]==0:
                continue
            grow[j] -= 1
            A[y][x] += j
            break
    
    for i in range(x0+1, x1+1):
        S[i] += 1
    for i in range(x1+1, M):
        S[i] += 2
    

for y in range(1, M):
    for x in range(1, M):
        A[y][x] += S[x]

for y in range(M):
    print(" ".join(map(str, A[y])))
# 공 넣기
N, M = map(int, input().split())
A = [0]*101
for m in range(M):
    i, j, k = map(int, input().split())
    while i <= j:
        A[i] = k
        i += 1
print(" ".join(list(map(str, A[1:N+1]))))
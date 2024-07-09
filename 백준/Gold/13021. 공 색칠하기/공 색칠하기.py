# 공 색칠하기
N, M = map(int, input().split())
A = [-1] * N

# 색칠하기
for i in range(M):
    L, R = map(int, input().split())
    for j in range(L-1, R):
        A[j] = i

# 개수 세기
ans = 1
color = [False] * M
i = 0

while i<N:
    if A[i]==-1 or color[A[i]]:
        i += 1
    else:
        temp = A[i]
        color[temp] = True
        ans  *= 2
        while i<N and A[i]==temp:
            i += 1

print(ans)
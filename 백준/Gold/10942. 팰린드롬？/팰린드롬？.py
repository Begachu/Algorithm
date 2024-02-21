# 팰린드롬 골드4
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
C = [[False for x in range(N)] for y in range(N)]
answer = []

# 길이가 1인 배열은 무조건 팰린드롬
for i in range(N):
    C[i][i] = True

# 길이가 2인 배열은 시작과 끝이 동일하면 팰린드롬
for i in range(N-1):
    if A[i] == A[i+1]:
        C[i][i+1] = True

# 길이가 3이상인 배열은 
# 1) 시작과 끝이 동일하며,
# 2) 시작과 끝을 제외한 배열이 팰린드롬이면 팰린드롬
for len in range(2, N):
    for i in range(N-len):
        if A[i]==A[i+len] and C[i+1][i+len-1]:
            C[i][i+len] = True

for m in range(M):
    S, E = map(int, input().split())
    if C[S-1][E-1]:
        answer.append("1")
    else:
        answer.append("0")

print("\n".join(answer))
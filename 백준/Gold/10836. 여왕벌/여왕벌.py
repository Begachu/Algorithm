import sys
input = sys.stdin.readline

M, N = map(int, input().split())
S = [1 for _ in range(2*M-1)]


for _ in range(N):
    grow = list(map(int, input().split()))
    for i in range(grow[0], sum(grow[:2])):
        S[i] += 1
    for i in range(sum(grow[:2]), 2*M-1):
        S[i] += 2

string = " ".join(map(str, S[M:]))
for y in range(M):
    print(str(S[M-y-1])+" "+string)
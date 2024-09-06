# 영수증
X = int(input())
N = int(input())
S = 0

for n in range(N):
    a, b = map(int, input().split())
    S += a * b

print("Yes" if S==X else "No")
N = int(input())
ans = 0

for n in range(1, N+1):
    if N % n == 0:
        ans += n

print(ans * 5 - 24)
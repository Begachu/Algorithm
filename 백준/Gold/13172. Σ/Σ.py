import math
import sys
input = sys.stdin.readline

MOD = 1000000007
ans = 0

def dc(n, a):
    if a == 1:
        return n
    if a%2 == 0:
        temp = dc(n, a//2) % MOD
        return (temp * temp) % MOD
    else:
        temp = dc(n, a//2) % MOD
        return (temp * temp * n) % MOD

M = int(input())

for m in range(M):
    N, S = map(int, input().split())
    gcd = math.gcd(N, S)
    N = N//gcd
    S = S//gcd
    ans += (dc(N, MOD-2) * S) % MOD

print(ans % MOD)
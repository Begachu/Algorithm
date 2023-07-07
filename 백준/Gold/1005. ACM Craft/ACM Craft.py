# ACM Craft
import sys
from collections import deque
input = sys.stdin.readline

sys.setrecursionlimit(10000)
w = []
e = []
cnt = []

def dp(n):
    if cnt[n]!=-1:
        return cnt[n]
    if len(e[n])==0:
        cnt[n] = w[n]
    else:
        _max = 0
        for i in e[n]:
            temp = dp(i)
            if _max<temp:
                _max = temp
        cnt[n] = w[n]+_max
    return cnt[n]

T = int(input())
for t in range(T):
    (N, K) = list(map(int, input().split()))
    w = list(map(int, input().split()))
    e = [deque() for n in range(N)]
    cnt = [-1 for n in range(N)]
    for k in range(K):
        (u, v) = list(map(int, input().split()))
        e[v-1].append(u-1)
    end = int(input())-1
    print(dp(end))
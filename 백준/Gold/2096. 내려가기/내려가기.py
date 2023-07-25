import sys
input = sys.stdin.readline

N = int(input())
_min = [[0 for _ in range(3)] for __ in range(2)]
_max = [[0 for _ in range(3)] for __ in range(2)]

for n in range(N):
    A = list(map(int, input().split()))

    _min[n%2][0] = min(_min[(n+1)%2][0], _min[(n+1)%2][1]) + A[0]
    _min[n%2][1] = min(_min[(n+1)%2]) + A[1]
    _min[n%2][2] = min(_min[(n+1)%2][1], _min[(n+1)%2][2]) + A[2]

    _max[n%2][0] = max(_max[(n+1)%2][0], _max[(n+1)%2][1]) + A[0]
    _max[n%2][1] = max(_max[(n+1)%2]) + A[1]
    _max[n%2][2] = max(_max[(n+1)%2][1], _max[(n+1)%2][2]) + A[2]

print(max(_max[(N+1)%2]))
print(min(_min[(N+1)%2]))
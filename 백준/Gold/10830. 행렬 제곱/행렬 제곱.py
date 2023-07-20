N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]


def matmul(A1, A2):
    return [[sum([A1[n][i]*A2[i][m] for i in range(N)]) % 1000 for m in range(N)] for n in range(N)]


def dc(a, m):
    if m == 1:
        return a

    _a = dc(a, m//2)
    _a = matmul(_a, _a)

    if m % 2 == 1:
        _a = matmul(_a, A)

    return _a


answer = dc(A, M)

for line in answer:
    print(' '.join(list(map(str, [i % 1000 for i in line]))))
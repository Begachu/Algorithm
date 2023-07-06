(a, b, c, d, e, f) = list(map(int, input().split()))

def bf():
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if a*x + b*y == c and d*x + e*y == f:
                return x, y


(x, y) = bf()
print(x, y)
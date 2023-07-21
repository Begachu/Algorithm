# 어린 왕자
import sys
input = sys.stdin.readline

def mult(n):
    return n*n

T = int(input())
for t in range(T):
    (x1, y1, x2, y2) = list(map(int, input().split()))
    result = 0
    P = int(input())
    for p in range(P):
        (cx, cy, r) = list(map(int, input().split()))
        if mult(cx-x1)+mult(cy-y1)>mult(r) and mult(cx-x2)+mult(cy-y2)>mult(r):
            continue
        elif mult(cx-x1)+mult(cy-y1)>mult(r):
            result += 1
        elif mult(cx-x2)+mult(cy-y2)>mult(r):
            result += 1
    print(result)
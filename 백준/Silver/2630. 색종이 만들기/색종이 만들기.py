# 색종이 만들기
import sys
input = sys.stdin.readline

N = int(input())
paper = [input().strip().split() for n in range(N)]

def dc(n, x, y):
    if n==1:
        if paper[y][x]=='1':
            return (0, 1)
        else:
            return (1, 0)
    else:
        BLUE = True
        WHITE = True
        temp = [(x, y), (x+n//2, y), (x, y+n//2), (x+n//2, y+n//2)]
        blue, white = (0, 0)

        for _x, _y in temp:
            (_b, _w) = dc(n//2, _x, _y)
            if _w>0:
                BLUE = False
            if _b>0:
                WHITE = False
            blue += _b
            white += _w
        if BLUE and not WHITE:
            blue = 1
        elif WHITE and not BLUE:
            white = 1

        return (blue, white)

result = dc(N, 0, 0)
print(result[0])
print(result[1])
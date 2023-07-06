from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

if N==0:
    print(0)
else: 
    except_boundary = round(N * 0.15 + 0.0000001)
    arr = [int(input()) for i in range(N)]
    arr.sort()

    print(round(sum(arr[except_boundary : N - except_boundary])/(N-except_boundary*2) + 0.0000001))
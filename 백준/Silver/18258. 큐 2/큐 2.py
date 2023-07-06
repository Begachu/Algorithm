import sys
from collections import deque

input = sys.stdin.readline

queue = deque()
N = int(input())

for n in range(N):
    commend = input().split()
    if commend[0] == "push":
        queue.append(commend[1])
    elif commend[0] == "pop":
        if queue:
             print(queue.popleft())
        else:
            print(-1)
    elif commend[0] == "size":
        print(len(queue))
    elif commend[0] == "empty":
        print(0 if queue else 1)
    elif commend[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif commend[0] == "back":
        if queue:
            print(queue[len(queue)-1])
        else:
            print(-1)
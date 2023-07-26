from collections import deque
import sys
input = sys.stdin.readline

S = list(input().split("\n")[0])
B = input().split("\n")[0]

stack = deque()

for i in range(len(S)):
    flag = False

    if stack:
        arr = []
        
        if B[0] == S[i]:
            arr.append(0)

        for idx in stack[0][1]:
            nextIdx = idx + 1
            if B[nextIdx] == S[i]:
                arr.append(nextIdx)
        
        if arr:
          flag = True
          stack.appendleft((i, arr))
    
    elif B[0] == S[i]:
        flag = True
        stack.appendleft((i, [0]))
    
    if not flag:
        stack = deque()
    
    while stack and stack[0][1][-1] == len(B)-1:
      for b in B:
          idx, arr = stack.popleft()
          S[idx] = ""

S = "".join(S)

print(S if S!="" else "FRULA")
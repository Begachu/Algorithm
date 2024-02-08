import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

preorder = []
postorder = []

while True:
    try:
        preorder.append(int(input()))
    except:
        break
    

def search(start, end):
    flag = True

    for i in range(start+1, end):
        if preorder[i] > preorder[start]:
            if i > start+1:
                search(start+1, i)
                flag = False
            else:
                flag = False

            search(i, end)
            break
    
    if flag and start+1 < end:
        search(start+1, end)

    postorder.append(str(preorder[start]))

search(0, len(preorder))

print("\n".join(postorder))
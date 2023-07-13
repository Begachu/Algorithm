import sys
input = sys.stdin.readline


class Node:
    def __init__(self, val):
        self.val = val
        self.next = []

T = int(input())
A = []

for t in range(T):
  N = int(input())
  head = Node(None)
  leaves = []

  for n in range(N):
    string = input().split("\n")[0]
    p = head

    for chr in string:
      flag = True

      for node in p.next:
        if node.val == chr:
          p = node
          flag = False
          break
      
      if flag:
        node = Node(chr)
        p.next.append(node)
        p = node
    
    leaves.append(p)

  answer = True
  
  for node in leaves:
    if len(node.next) > 0:
      answer = False
      break
    
  A.append("YES" if answer else "NO")

for a in A:
  print(a)
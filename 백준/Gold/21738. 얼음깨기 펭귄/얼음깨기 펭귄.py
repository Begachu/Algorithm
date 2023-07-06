# GOLD 5: 얼음깨기 펭귄
from collections import deque
import sys
input = sys.stdin.readline

class Node:
  def __init__(self, id):
    self.id = id
    self.edges = []

(N, S, P) = list(map(int, input().split()))
nodes = [Node(n) for n in range(N+1)]
visited = [False for i in range(N+1)]
for n in range(N-1):
  (v, u) = list(map(int, input().split()))
  nodes[v].edges.append(u)
  nodes[u].edges.append(v)

visited[P] = True
q = deque([(P, 0)])

end = [0, 0]

while(q):
  (idx, depth) = q.popleft()
  if idx <= S:
    if end[0]==0:
      end[0] = depth
    else:
      end[1] = depth
      break

  for nextIdx in nodes[idx].edges:
    if not visited[nextIdx]:
      q.append((nextIdx, depth+1))
      visited[nextIdx] = True

print(N - end[0] - end[1] - 1)
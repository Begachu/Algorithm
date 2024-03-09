import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

class Node:
    def __init__(self, no):
        self.no = no
        self.edge = []
        self.value = 1
    def appendEdge(self, no):
        self.edge.append(no)
    def setValue(self, value):
        self.value = value
    def getValue(self):
        return self.value

N, R, Q = map(int, input().split())
nodes = [Node(i) for i in range(N+1)]
answer = []

for _ in range(N-1):
    U, V = map(int, input().split())
    nodes[U].appendEdge(V)
    nodes[V].appendEdge(U)

visited = [False] * (N+1)
visited[R] = True

def recursion(u):
    value = 1

    for v in nodes[u].edge:
        if visited[v]:
            continue
        visited[v] = True
        value += recursion(v)

    nodes[u].setValue(value)
    return value

recursion(R)

for _ in range(Q):
    U = int(input())
    answer.append(str(nodes[U].getValue()))

print("\n".join(answer))
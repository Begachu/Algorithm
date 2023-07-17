# 웜홀
import sys
from collections import deque
input = sys.stdin.readline

TC = int(input())
for tc in range(TC):
	N, M, W = map(int, input().split())
	Node = [sys.maxsize]*N
	Edge = [[] for i in range(N)]
	answer = False
	
	# Save Edge
	for m in range(M):
		S, E, T = map(int, input().split())
		Edge[S-1].append((E-1, T))
		Edge[E-1].append((S-1, T))
	for w in range(W):
		S, E, T = map(int, input().split())
		Edge[S-1].append((E-1, -T))
		
	# Compute
	for n in range(N):
		if Node[n]!=sys.maxsize:
			continue
		queue = deque()
		Node[n] = 0
		for edge in Edge[n]:
			v, e = edge
			Node[v] = e
			queue.append((1, v, e))
		while queue:
			_N, _V, _E = queue.popleft()
			if Node[_V]!=_E:
				continue
			if _N==N:
				answer = True
				break
			for edge in Edge[_V]:
				v, e = edge
				if Node[v]>e+_E:
					Node[v] = e+_E
					queue.append((_N+1, v, _E+e))
		if answer:
			break
	if answer:
		print("YES")
	else:
		print("NO")
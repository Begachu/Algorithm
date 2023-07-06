from collections import deque

(N, M) = list(map(int, input().split()))
target = list(map(int, input().split()))
q = deque([i+1 for i in range(N)])
answer = 0

for t in target:
    if q[0] != t:
        for i in range(1, len(q)):
            answer += 1
            
            if q[i] == t:
                while q[0] != t:
                    q.append(q.popleft())
                break
            elif q[len(q)-i] == t:
                while q[0] != t:
                    q.appendleft(q.pop())
                break
    q.popleft()
    
print(answer)
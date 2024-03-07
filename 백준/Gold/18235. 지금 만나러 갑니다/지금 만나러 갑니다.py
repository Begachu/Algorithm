from collections import deque

N, A, B = map(int, input().split())

answer = -1
S = [1]*20
S[2] = 2
for i in range(3, 20):
    S[i] = S[i-1] * 2

qa = deque([(0, A)])
qb = deque([(0, B)])

for i in range(1, 20):
    visited = [False]*(N+1)
    while qa and qa[0][0]<i:
        ad, a = qa.popleft()
        visited[a] = True
        if a+S[i]<=N:
            qa.append((i, a+S[i]))
        if a-S[i]>0:
            qa.append((i, a-S[i]))

    while qb and qb[0][0]<i:
        bd, b = qb.popleft()
        if visited[b] == True:
            answer = bd
            break
        if b+S[i]<=N:
            qb.append((i, b+S[i]))
        if b-S[i]>0:
            qb.append((i, b-S[i]))
    
    if answer!=-1:
        break

print(answer)
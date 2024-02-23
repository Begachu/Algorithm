from collections import deque

# 소수의 연속합 :GOLD 3
N = int(input())
answer = 0
A = [True for _ in range(N+1)]
temp = 0
stack = deque()

# 에라토스테네스의 체를 통해 소수 구하기
for i in range(2, N+1):
    if not A[i]:
        continue

    for k in range(i*2, N+1, i):
        A[k] = False
    
    # 소수만 따로 저장
    stack.append(i)

    temp += i
    while temp > N and stack:
        temp -= stack.popleft()
        
    if temp == N:
        answer += 1

print(answer)
N, M = map(int, input().split())
cnt = [False for i in range(10001)]
A = []

for item in list(map(int, input().split())):
  cnt[item] = True

for i in range(10001):
  if cnt[i]:
    A.append(str(i))

def bt(m, idx, ans):
  if m==M:
    print(ans)
    return
  
  for i in range(idx, len(A)):
    bt(m+1, i, ans+A[i]+" ")

bt(0, 0, "")
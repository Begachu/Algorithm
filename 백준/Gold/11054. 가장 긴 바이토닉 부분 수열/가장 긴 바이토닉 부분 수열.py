N = int(input())
A = [0] + list(map(int, input().split()))
cnt = [[-1 for n in range(N+1)] for i in range(2)]

def dp(i, t, up):
  if i > N:
    return 0
  
  if cnt[up][t] == -1:

    if up==0:
      if A[t] < A[i]:
        cnt[up][t] = max(dp(i+1, i, 0)+1, dp(i+1, t, 0))
      elif A[t] > A[i]:
        cnt[up][t] = max(dp(i+1, i, 1)+1, dp(i+1, t, 0))
      else:
        cnt[up][t] = dp(i+1, t, 0)
    
    else:
      if A[t] > A[i]:
        cnt[up][t] = max(dp(i+1, i, 1)+1, dp(i+1, t, 1))
      else:
        cnt[up][t] = dp(i+1, t, 1)
  
  return cnt[up][t]

print(dp(1, 0, 0))
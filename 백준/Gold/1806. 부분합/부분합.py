# 부분합
N, S = map(int, input().split())
A = list(map(int, input().split()))
ans = -1

temp, p1, p2 = (0, 0, 0)

while p2<N:
    temp += A[p2]
    p2 += 1
    
    # 기준 미달
    if temp < S:
        continue

    # ans 갱신
    if ans == -1:
        ans = p2 - p1
    else:
        ans = min(ans, p2 - p1)

    while p1 < p2:
        temp -= A[p1]
        p1 += 1

        if temp < S:
            break

        ans = min(ans, p2 - p1)


print(ans if ans > 0 else 0)
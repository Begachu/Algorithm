import sys
input = sys.stdin.readline

T = int(input())
answer = [4 * 3 for t in range(T)]
MBTI = {"ISTJ": 0, "ISTP": 1, "ESTP": 2, "ESTJ": 3,
        "INTJ": 4, "INTP": 5, "ENTP": 6, "ENTJ": 7,
        "INFJ": 8, "INFP": 9, "ENFP": 10, "ENFJ": 11,
        "ISFJ": 12, "ISFP": 13, "ESFP": 14, "ESFJ": 15}

gap = [0, 1, 2, 1]

for t in range(T):
    N = int(input())
    arr = input().split()
    cnt = [0 for i in range(16)]
    
    for n in range(N):
        cnt[MBTI[arr[n]]] += 1

    for i in range(16):
        if cnt[i] == 0:
            continue
        
        cnt[i] -= 1
        for j in range(i, 16):
            if cnt[j] == 0:
                continue
            
            cnt[j] -= 1
            for k in range(j, 16):
                if cnt[k] == 0:
                    continue
                
                cnt[k] -= 1
                
                i2j = gap[(j%4 - i%4)] + gap[(j//4 - i//4)]
                i2k = gap[(k%4 - i%4)] + gap[(k//4 - i//4)]
                j2k = gap[(k%4 - j%4)] + gap[(k//4 - j//4)]

                answer[t] = min(answer[t], i2j + i2k + j2k)

                cnt[k] += 1
            cnt[j] += 1
        cnt[i] += 1
    
for ans in answer:
    print(ans)
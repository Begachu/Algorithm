import sys
input = sys.stdin.readline

N = int(input())
image = [list(input().strip()) for i in range(N)]

def dp(n, x, y):
	if n==1:
		return image[x][y]
	S = ''
	_x = [x, x, x+n//2, x+n//2]
	_y = [y, y+n//2, y, y+n//2]
	
	for i in range(4):
		S += dp(n//2, _x[i], _y[i])
	if S=='1111':
		S = '1'
	elif S=='0000':
		S = '0'
	else:
		S = '('+S+')'
	return S
	
print(dp(N,0,0))
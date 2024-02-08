star = ["  *  ", " * * ", "*****"]
h = 3
k = int(input())//3

while k>1:
    _star = [star[i]+" "+star[i] for i in range(h)]
    star = [" "*h+star[i]+" "*h for i in range(h)] + _star
    h *= 2
    k //= 2

print("\n".join(star))
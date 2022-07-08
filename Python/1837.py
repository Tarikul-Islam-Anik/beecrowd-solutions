a, b = map(int, input().split())

if b < 0:
    print((a//abs(b))*-1, a % abs(b))
else:
    print(a//b, a % b)

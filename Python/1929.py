def isTriangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


a, b, c, d = map(int, input().split())

r = []

for i in range(4):
    if i == 0:
        if isTriangle(a, b, c):
            r.append(1)
    elif i == 1:
        if isTriangle(a, b, d):
            r.append(1)
    elif i == 2:
        if isTriangle(a, c, d):
            r.append(1)
    else:
        if isTriangle(b, c, d):
            r.append(1)

if 1 in r:
    print("S")
else:
    print("N")

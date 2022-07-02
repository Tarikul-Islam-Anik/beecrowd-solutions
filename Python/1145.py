x, y = map(int, input().split())

if x > y:
    x, y = y, x

for i in range(1, y + 1):
    if i % x == 0:
        print(i)
    else:
        print(i, end=" ")

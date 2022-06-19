x = int(input())
y = int(input())

odds = []

if y < x:
    for i in range(y + 1, x):
        if i % 2 != 0:
            odds.append(i)
else:
    for i in range(x + 1, y):
        if i % 2 != 0:
            odds.append(i)

print(sum(odds))

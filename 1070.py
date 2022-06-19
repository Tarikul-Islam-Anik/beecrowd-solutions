n = int(input())

odds = []

while True:
    if len(odds) == 6:
        break
    else:
        if n % 2 != 0:
            odds.append(n)
            n += 1
        else:
            n += 1

[print(i) for i in odds]

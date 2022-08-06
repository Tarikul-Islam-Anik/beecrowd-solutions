odds = []
evens = []

for i in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

[print(i) for i in sorted(evens)]
[print(i) for i in sorted(odds, reverse=True)]

n, m = map(int, input().split())

for i in range(m):
    msg = input()
    if msg == 'clicou':
        n -= 1
    else:
        n += 1


print(n)

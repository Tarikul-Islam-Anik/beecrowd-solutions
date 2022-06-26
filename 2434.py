n, s = map(int, input().split())
balance = s

for i in range(n):
    s += int(input())
    if s < balance:
        balance = s


print(balance)

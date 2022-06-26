lst = list(map(int, input().split()))

lst.sort(reverse=True)

a = lst[0]
n = lst[1]

s = 0

for i in range(n):
    s += a
    a += 1

print(s)

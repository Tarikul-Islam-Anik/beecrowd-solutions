loop = int(input())

c = 0
r = 0
s = 0

for i in range(loop):
    n = input().split()
    if n[1] == "C":
        c += int(n[0])
    elif n[1] == "R":
        r += int(n[0])
    elif n[1] == "S":
        s += int(n[0])


total = c + r + s

print("Total:", total, "cobaias")
print("Total de coelhos:", c)
print("Total de ratos:", r)
print("Total de sapos:", s)
print("Percentual de coelhos: %.2f" % (c * 100 / total), "%")
print("Percentual de ratos: %.2f" % (r * 100 / total), "%")
print("Percentual de sapos: %.2f" % (s * 100 / total), "%")

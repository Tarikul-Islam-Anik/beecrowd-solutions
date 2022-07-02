s = 0
count = 0

while count < 2:
    n = float(input())
    if 0 <= n <= 10:
        s += n
        count += 1
    else:
        print("nota invalida")

print("media = {:.2f}".format(s / 2))

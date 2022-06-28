x = z = 0

x = int(input())
while True:
    z = int(input())
    if x < z:
        break

s = 0
count = 0

while s < z:
    s += x
    x += 1
    count += 1

print(count)

in_count = 0
out_count = 0

loop = int(input())

for i in range(loop):
    n = int(input())

    if 10 <= n <= 20:
        in_count += 1
    else:
        out_count += 1

print(in_count, "in")
print(out_count, "out")

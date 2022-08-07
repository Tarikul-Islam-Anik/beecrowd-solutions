n = int(input())

if n == 1:
    x = 0.1666666667
if n == 0:
    x = 0.0000000000

for i in range(2, n + 1):
    if i == 2:
        x = 6.0 + (1.00 / 6.00)
        x = 1.00 / x
    else:
        x = 6.00 + x
        x = 1.00 / x

x = x + 3.00
print(f"{x:.10f}")

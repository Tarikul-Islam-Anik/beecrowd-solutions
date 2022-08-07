n = int(input())

if n == 1:
    x = 0.5000000000
if n == 0:
    x = 0.0000000000

for i in range(2, n + 1):
    if i == 2:
        x = 2.0 + 0.5
        x = 1.0 / x
    else:
        x = 2.0 + x
        x = 1.0 / x

x = x + 1.00
print(f"{x:.10f}")

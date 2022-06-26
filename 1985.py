price = {
    1001: 1.50,
    1002: 2.50,
    1003: 3.50,
    1004: 4.50,
    1005: 5.50,
}

s = 0

for i in range(int(input())):
    item, qty = map(int, input().split())
    s += price[item] * qty

print(f"{s:.2f}")

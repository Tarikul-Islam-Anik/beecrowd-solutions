def gcd(n, d):
    if n % d == 0:
        return d
    else:
        return gcd(d, n % d)


t = int(input())

nums = []

for i in range(t):
    nums.append(input())

for i in nums:
    operator_idx = int(len(i) / 2)
    if i[operator_idx] == "+":
        n1, d1 = i[:operator_idx].split("/")
        n2, d2 = i[operator_idx + 1 :].split("/")
        n = int(n1) * int(d2) + int(n2) * int(d1)
        d = int(d1) * int(d2)
        lhs = f"{n}/{d}"
        n, d = n // gcd(n, d), d // gcd(n, d)
        print(f"{lhs} = {n}/{d}")

    elif i[operator_idx] == "-":
        n1, d1 = i[:operator_idx].split("/")
        n2, d2 = i[operator_idx + 1 :].split("/")
        n = int(n1) * int(d2) - int(n2) * int(d1)
        d = int(d1) * int(d2)
        lhs = f"{n}/{d}"
        n, d = n // gcd(n, d), d // gcd(n, d)
        print(f"{lhs} = {n}/{d}")
    elif i[operator_idx] == "*":
        n1, d1 = i[:operator_idx].split("/")
        n2, d2 = i[operator_idx + 1 :].split("/")
        n = int(n1) * int(n2)
        d = int(d1) * int(d2)
        lhs = f"{n}/{d}"
        n, d = n // gcd(n, d), d // gcd(n, d)
        print(f"{lhs} = {n}/{d}")
    elif i[operator_idx] == "/":
        n1, d1 = i[:operator_idx].split("/")
        n2, d2 = i[operator_idx + 1 :].split("/")
        n = int(n1) * int(d2)
        d = int(d1) * int(n2)
        lhs = f"{n}/{d}"
        n, d = n // gcd(n, d), d // gcd(n, d)
        print(f"{lhs} = {n}/{d}")

def fibonacci(n):
    a, b = 0, 1
    lst = []
    for i in range(n):
        a, b = b, a + b
        lst.append(a)
    return lst[::-1]


print(" ".join(map(str, fibonacci(int(input())))))

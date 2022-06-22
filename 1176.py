def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


for i in range(int(input())):
    n = int(input())
    print(f"Fib({n}) = {fib(n)}")

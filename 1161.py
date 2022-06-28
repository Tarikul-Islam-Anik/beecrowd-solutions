while True:
    try:
        m, n = map(int, input().split())
        print(__import__("math").factorial(m) + __import__("math").factorial(n))
    except EOFError:
        break
